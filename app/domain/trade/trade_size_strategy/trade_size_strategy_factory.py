from app.config.env import FIXED_TRADE_SIZE
from app.domain.trade.trade_size_strategy.proportional_trade_size_strategy import ProportionalTradeSizeStrategy
from app.domain.trade.trade_size_strategy.target_trade_size_strategy import TargetTradeSizeStrategy
from app.domain.trade.trade_size_strategy.trade_size_strategy import TradeSizeStrategy, TradeSizeStrategyType
from app.domain.trade.trade_size_strategy.fixed_trade_size_strategy import FixedTradeSizeStrategy


def create_trade_size_strategy(strategy: TradeSizeStrategyType) -> TradeSizeStrategy:
    match strategy:
        case TradeSizeStrategyType.FIXED:
            return FixedTradeSizeStrategy(FIXED_TRADE_SIZE)
        case TradeSizeStrategyType.PROPORTIONAL:
            return ProportionalTradeSizeStrategy()
        case TradeSizeStrategyType.TARGET:
            return TargetTradeSizeStrategy()
        case _:
            raise ValueError(f"Unsupported trade size strategy type: {strategy}")