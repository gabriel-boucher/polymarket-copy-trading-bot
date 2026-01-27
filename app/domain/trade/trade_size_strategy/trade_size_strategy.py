from abc import abstractmethod, ABC
from enum import Enum

from app.domain.trade.trade import Trade

class TradeSizeStrategyType(Enum):
    FIXED = "fixed"
    PROPORTIONAL = "proportional"
    TARGET = "target"

class TradeSizeStrategy(ABC):
    @abstractmethod
    def calculate_size(self, target_trade: Trade, user_balance: float, target_balance: float) -> float:
        pass