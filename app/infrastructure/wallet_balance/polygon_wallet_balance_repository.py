from typing import Any

from web3 import Web3

from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.wallet_balance_repository import WalletBalanceRepository


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
    __web3: Web3
    __decimals: int

    def __init__(self, web3: Web3) -> None:
        self.__web3 = web3
        self.__decimals = -1

    def get_wallet_balance_by_address(self, wallet_address: WalletAddress) -> float:
        contract = self.__web3.eth.contract(
            address=self.__USDC_CONTRACT_ADDRESS.to_web3(),
            abi=self.__ERC20_ABI
        )

        raw_balance = contract.functions.balanceOf(wallet_address.to_web3()).call()

        if self.__decimals == -1:
            self.__decimals = contract.functions.decimals().call()

        balance: float = raw_balance / (10 ** self.__decimals)

        return balance
