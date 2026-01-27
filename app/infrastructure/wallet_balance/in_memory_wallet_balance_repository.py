from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.wallet_balance_repository import WalletBalanceRepository


class InMemoryWalletBalanceRepository(WalletBalanceRepository):
    __wallet_balances: dict[WalletAddress, float]

    def __init__(self, user_address: WalletAddress, target_address: WalletAddress) -> None:
        self.__wallet_balances = {
            user_address: 1000.0,
            target_address: 5000.0
        }

    def get_wallet_balance_by_address(self, wallet_address: WalletAddress) -> float:
        balance: float = self.__wallet_balances.get(wallet_address, 0.0)
        return balance