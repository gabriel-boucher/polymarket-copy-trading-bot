from abc import ABC, abstractmethod

from app.domain.wallet_address import WalletAddress
from app.domain.trade.trade import Trade


class TradeRepository(ABC):
    @abstractmethod
    def get_last_trade_by_wallet_address(self, wallet_address: WalletAddress) -> Trade:
        pass

    @abstractmethod
    def get_trades_by_wallet_address(self, wallet_address: WalletAddress, limit: int=1) -> list[Trade]:
        pass

    @abstractmethod
    def save_trade(self, trade: Trade) -> None:
        pass
