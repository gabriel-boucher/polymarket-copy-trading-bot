from app.domain.trade.trade_size_strategy.trade_size_strategy import TradeSizeStrategy
from app.domain.trade.trade import Trade

class TradeFactory:
    __trade_size_strategy: TradeSizeStrategy

    def __init__(self, trade_size_strategy: TradeSizeStrategy) -> None:
        self.__trade_size_strategy = trade_size_strategy

    def create_trade(self, target_trade: Trade, user_balance: float, target_balance: float) -> Trade:
        user_trade_size: float = self.__trade_size_strategy.calculate_size(target_trade, user_balance, target_balance)

        return Trade(
            token_id=target_trade.token_id,
            price=target_trade.price,
            size=user_trade_size,
            side=target_trade.side,
            wallet_address=target_trade.wallet_address,
            condition_id=target_trade.condition_id,
            outcome=target_trade.outcome,
            timestamp=target_trade.timestamp
        )