from py_clob_client import ClobClient

from app.config.config import Config
from app.infrastructure.trade.polymarket.clob_client_factory import create_clob_client
from app.infrastructure.trade.polymarket.polymarket_trade_repository import PolymarketTradeRepository
from app.infrastructure.wallet_balance.polymarket.rpc_wallet_balance_repository import PolygonWalletBalanceRepository
from app.infrastructure.wallet_balance.polymarket.rpc_provider import RpcProvider
from app.infrastructure.wallet_balance.polymarket.rpc_provider_factory import create_rpc_provider


class PolymarketConfig(Config):
    def __init__(self) -> None:
        client: ClobClient = create_clob_client()
        rpc_provider: RpcProvider[float] = create_rpc_provider()

        self._trade_repository = PolymarketTradeRepository(client)
        self._wallet_balance_repository = PolygonWalletBalanceRepository(rpc_provider)
        super().__init__()