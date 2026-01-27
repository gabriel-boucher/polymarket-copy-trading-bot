from pydantic import BaseModel, Field


class TradePolymarketDto(BaseModel):
    token_id: str = Field(alias="asset")
    price: float
    size: float
    side: str
    condition_id: str = Field(alias="conditionId")
    outcome: str
    timestamp: int

    model_config = {
        "populate_by_name": True
    }