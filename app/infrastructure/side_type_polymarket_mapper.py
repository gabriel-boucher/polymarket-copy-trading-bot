from app.domain.side_type import SideType


def to_side_type_domain(side_type_polymarket_dto: str) -> SideType:
    match side_type_polymarket_dto:
        case "BUY":
            return SideType.BUY
        case "SELL":
            return SideType.SELL
        case "":
            return SideType.NONE
        case _:
            raise ValueError(f"Unknown side type: {side_type_polymarket_dto}")

def to_side_type_polymarket_dto(side_type: SideType) -> str:
    match side_type:
        case SideType.BUY:
            return "BUY"
        case SideType.SELL:
            return "SELL"
        case SideType.NONE:
            return ""
        case _:
            raise ValueError(f"Unknown side type: {side_type}")