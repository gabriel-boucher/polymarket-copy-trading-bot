from typing import Any

from web3 import Web3
from web3.contract import Contract

from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.wallet_balance_repository import WalletBalanceRepository
from app.infrastructure.wallet_balance.polymarket.rpc_provider import RpcProvider


class PolygonWalletBalanceRepository(WalletBalanceRepository):
    __USDC_CONTRACT_ADDRESS: WalletAddress = WalletAddress("0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174")
    __ERC20_ABI: list[Any] = [
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "decimals",
            "outputs": [{"name": "", "type": "uint8"}],
            "type": "function",
        }
    ]
    __rpc_provider: RpcProvider[float]
    __decimals: int

    def __init__(self, rpc_provider: RpcProvider[float]) -> None:
        self.__rpc_provider = rpc_provider
        self.__decimals = -1

    def get_wallet_balance_by_address(self, wallet_address: WalletAddress) -> float:
        def _call(web3: Web3) -> float:
            contract: Contract = web3.eth.contract(
                address=self.__USDC_CONTRACT_ADDRESS.to_web3(),
                abi=self.__ERC20_ABI
            )

            raw_balance = contract.functions.balanceOf(wallet_address.to_web3()).call()

            self.__set_wallet_balance_decimals(contract)

            balance: float = raw_balance / (10 ** self.__decimals)

            return balance

        return self.__rpc_provider.execute(_call)

    def __set_wallet_balance_decimals(self, contract: Contract) -> None:
        if self.__decimals == -1:
            self.__decimals = contract.functions.decimals().call()
