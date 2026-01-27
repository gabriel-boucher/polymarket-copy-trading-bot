from app.domain.condition_id import ConditionId
from app.domain.token_id import TokenId
from app.domain.trade.trade import Trade
from app.infrastructure.side_type_polymarket_mapper import to_side_type_polymarket_dto, to_side_type_domain
from app.infrastructure.trade.trade_polymarket_dto import TradePolymarketDto


def to_trade_polymarket_dto(trade: Trade) -> TradePolymarketDto:
    return TradePolymarketDto(
        asset=str(trade.token_id),
        price=trade.price,
        size=trade.size,
        side=to_side_type_polymarket_dto(trade.side),
        conditionId=str(trade.condition_id),
        outcome=trade.outcome,
        timestamp=trade.timestamp,
    )

def to_trade_domain(trade_dto: TradePolymarketDto) -> Trade:
    return Trade(
        token_id=TokenId(trade_dto.token_id),
        price=trade_dto.price,
        size=trade_dto.size,
        side=to_side_type_domain(trade_dto.side),
        condition_id=ConditionId(trade_dto.condition_id),
        outcome=trade_dto.outcome,
        timestamp=trade_dto.timestamp,
    )