from app.domain.trade.exceptions.insufficient_balance_exception import InsufficientBalanceException
from app.domain.trade.trade_size_strategy.trade_size_strategy import TradeSizeStrategy
from app.domain.trade.trade import Trade


class TargetTradeSizeStrategy(TradeSizeStrategy):
    def calculate_size(self, target_trade: Trade, user_balance: float, target_balance: float) -> float:
        if target_trade.size > user_balance:
            raise InsufficientBalanceException(target_trade.size, target_trade.wallet_address)

        return target_trade.size