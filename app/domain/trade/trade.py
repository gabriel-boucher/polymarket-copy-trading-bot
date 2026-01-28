from dataclasses import dataclass

from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.wallet_address import WalletAddress


@dataclass
class Trade:
    token_id: TokenId
    price: float
    size: float
    side: SideType
    wallet_address: WalletAddress
    condition_id: ConditionId
    outcome: str
    timestamp: int

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Trade):
            return False

        return (
            self.token_id == o.token_id and
            self.price == o.price and
            self.size == o.size and
            self.side == o.side and
            self.wallet_address == o.wallet_address and
            self.condition_id == o.condition_id and
            self.outcome == o.outcome and
            self.timestamp == o.timestamp
        )