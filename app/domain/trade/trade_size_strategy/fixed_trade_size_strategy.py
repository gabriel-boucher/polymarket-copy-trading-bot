from app.domain.trade.exceptions.insufficient_balance_exception import InsufficientBalanceException
from app.domain.trade.trade_size_strategy.trade_size_strategy import TradeSizeStrategy
from app.domain.trade.trade import Trade


class FixedTradeSizeStrategy(TradeSizeStrategy):
    __size: float

    def __init__(self, size: float) -> None:
        self.__size = size

    def calculate_size(self, target_trade: Trade, user_balance: float, target_balance: float) -> float:
        if self.__size > user_balance:
            raise InsufficientBalanceException(self.__size, target_trade.wallet_address)

        return self.__size