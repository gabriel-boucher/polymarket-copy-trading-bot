from dataclasses import dataclass

from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId


@dataclass
class Trade:
    token_id: TokenId
    price: float
    size: float
    side: SideType
    condition_id: ConditionId
    outcome: str
    timestamp: int