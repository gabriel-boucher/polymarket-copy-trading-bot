from typing import Any

from web3 import Web3
from web3.contract import Contract

from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.wallet_balance_repository import WalletBalanceRepository
from app.infrastructure.wallet_balance.rpc.rpc_provider import RpcProvider
from app.infrastructure.wallet_balance.rpc.wallet_balance_rpc_mapper import to_wallet_balance_domain


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
    __rpc_provider: RpcProvider[int]
    __decimals: int | None

    def __init__(self, rpc_provider: RpcProvider[int]) -> None:
        self.__rpc_provider = rpc_provider
        self.__decimals = None

    def get_wallet_balance_by_address(self, wallet_address: WalletAddress) -> float:
        raw_balance: int = self.__rpc_provider.execute(
            lambda web3: self.__get_raw_balance(web3, wallet_address)
        )

        decimals: int = self.__rpc_provider.execute(
            lambda web3: self.__get_decimals(web3)
        )

        balance: float = to_wallet_balance_domain(raw_balance, decimals)

        return balance

    def __get_raw_balance(self, web3: Web3, wallet_address: WalletAddress) -> int:
        contract: Contract = self.__get_contract(web3)

        raw_balance: int = contract.functions.balanceOf(wallet_address.to_web3()).call()

        return raw_balance

    def __get_decimals(self, web3: Web3) -> int:
        contract: Contract = self.__get_contract(web3)

        if self.__decimals is None:
            self.__decimals = contract.functions.decimals().call()

        return self.__decimals

    def __get_contract(self, web3: Web3) -> Contract:
        contract: Contract = web3.eth.contract(
            address=self.__USDC_CONTRACT_ADDRESS.to_web3(),
            abi=self.__ERC20_ABI
        )
        return contract