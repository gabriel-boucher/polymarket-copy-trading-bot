from typing import Final, Any

import requests
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs
from requests import Response

from app.domain.wallet_address import WalletAddress
from app.domain.trade.trade import Trade
from app.domain.trade.trade_repository import TradeRepository
from app.infrastructure.trade.trade_polymarket_dto import TradePolymarketDto
from app.infrastructure.trade.trade_polymarket_mapper import to_trade_polymarket_dto, to_trade_domain


class PolymarketTradeRepository(TradeRepository):
    __BASE_URL: Final[str] = "https://data-api.polymarket.com/trades"

    __client: ClobClient

    def __init__(self, client: ClobClient) -> None:
        super().__init__()
        self.__client = client

    def get_last_trade_by_wallet_address(self, wallet_address: WalletAddress) -> Trade:
        return self.get_trades_by_wallet_address(wallet_address)[0]

    def get_trades_by_wallet_address(self, wallet_address: WalletAddress, limit: int=1) -> list[Trade]:
        payload: dict[str, Any] = {
            "limit": limit,
            "takerOnly": False,
            "user": str(wallet_address)
        }
        response: Response = requests.get(self.__BASE_URL, params=payload)

        user_trades: list[Trade] = [to_trade_domain(
            TradePolymarketDto.model_validate(trade)
        ) for trade in response.json()]

        return user_trades

    def save_trade(self, trade: Trade) -> None:
        trade_dto: TradePolymarketDto = to_trade_polymarket_dto(trade)

        self.__client.create_and_post_order(
            OrderArgs(
                token_id=trade_dto.token_id,
                price=trade_dto.price,
                size=trade_dto.size,
                side=trade_dto.side
            )
        )



