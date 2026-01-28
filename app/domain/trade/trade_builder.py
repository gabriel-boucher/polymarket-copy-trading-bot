import datetime
import random
import uuid

from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.trade import Trade
from app.domain.wallet_address import WalletAddress


def build_trade() -> Trade:
    return Trade(
        token_id=TokenId(str(uuid.uuid4())),
        price=round(random.random(), 2),
        size=round(random.uniform(1, 100), 2),
        side=random.choice([SideType.BUY, SideType.SELL]),
        wallet_address=WalletAddress(str(uuid.uuid4())),
        condition_id=ConditionId(str(uuid.uuid4())),
        outcome=random.choice(["YES", "NO"]),
        timestamp=int(datetime.datetime.now().timestamp())
    )