from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.trade import Trade
from app.domain.trade.trade_builder import build_trade
from app.domain.trade.trade_repository import TradeRepository
from app.domain.wallet_address import WalletAddress


class InMemoryTradeRepository(TradeRepository):
    __user_address: WalletAddress
    __trades: dict[WalletAddress, list[Trade]]

    def __init__(self, user_address: WalletAddress, target_address: WalletAddress) -> None:
        self.__user_address = user_address
        self.__trades = {
            user_address: [build_trade()],
            target_address: [build_trade()]
        }

    def get_last_trade_by_wallet_address(self, wallet_address: WalletAddress) -> Trade:
        return self.__trades.get(wallet_address, [])[0]

    def get_trades_by_wallet_address(self, wallet_address: WalletAddress, limit: int = 1) -> list[Trade]:
        return self.__trades.get(wallet_address, [])[:limit]

    def save_trade(self, trade: Trade) -> None:
        self.__trades.setdefault(self.__user_address, []).append(trade)