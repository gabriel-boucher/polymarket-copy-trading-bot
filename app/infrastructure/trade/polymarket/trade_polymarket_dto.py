from pydantic import BaseModel, Field


class TradePolymarketDto(BaseModel):
    token_id: str = Field(alias="asset")
    price: float
    size: float
    side: str
    wallet_address: str = Field(alias="proxyWallet")
    condition_id: str = Field(alias="conditionId")
    outcome: str
    timestamp: int

    model_config = {
        "populate_by_name": True
    }