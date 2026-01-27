from abc import ABC, abstractmethod

from app.domain.wallet_address import WalletAddress


class WalletBalanceRepository(ABC):
    @abstractmethod
    def get_wallet_balance_by_address(self, wallet_address: WalletAddress) -> float:
        pass