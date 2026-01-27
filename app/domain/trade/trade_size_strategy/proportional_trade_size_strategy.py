from app.domain.trade.trade_size_strategy.trade_size_strategy import TradeSizeStrategy
from app.domain.trade.trade import Trade


class ProportionalTradeSizeStrategy(TradeSizeStrategy):
    def calculate_size(self, target_trade: Trade, user_balance: float, target_balance: float) -> float:
        return user_balance / target_balance * target_trade.size