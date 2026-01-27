from py_clob_client import ClobClient
from web3 import Web3

from app.config.config import Config
from app.infrastructure.clob_client_factory import create_clob_client
from app.infrastructure.polygon_web3_factory import create_polygon_web3
from app.infrastructure.trade.polymarket_trade_repository import PolymarketTradeRepository
from app.infrastructure.wallet_balance.polygon_wallet_balance_repository import PolygonWalletBalanceRepository


class PolymarketConfig(Config):
    def __init__(self) -> None:
        client: ClobClient = create_clob_client()
        web3: Web3 = create_polygon_web3()

        self._trade_repository = PolymarketTradeRepository(client)
        self._wallet_balance_repository = PolygonWalletBalanceRepository(web3)
        super().__init__()