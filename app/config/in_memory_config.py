from app.config.config import Config
from app.infrastructure.trade.in_memory_trade_repository import InMemoryTradeRepository
from app.infrastructure.wallet_balance.in_memory_wallet_balance_repository import InMemoryWalletBalanceRepository


class InMemoryConfig(Config):
    def __init__(self) -> None:
        super().__init__()
        self._trade_repository = InMemoryTradeRepository(self._user_address, self._target_address)
        self._wallet_balance_repository = InMemoryWalletBalanceRepository(self._user_address, self._target_address)
