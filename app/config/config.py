from app.application.trader_app_service import TraderAppService
from app.config.env import USER_ADDRESS, TARGET_ADDRESS, TRADE_SIZE_STRATEGY
from app.domain.trade.trade_size_strategy.trade_size_strategy import TradeSizeStrategyType
from app.domain.trade.trade_size_strategy.trade_size_strategy_factory import create_trade_size_strategy
from app.domain.trade.trade_factory import TradeFactory
from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.wallet_balance_repository import WalletBalanceRepository
from app.domain.trade.trade_repository import TradeRepository
from app.interfaces.trader_resource import TraderResource


class Config:
    _user_address: WalletAddress
    _target_address: WalletAddress
    _trade_size_strategy_type: TradeSizeStrategyType

    _trade_repository: TradeRepository
    _wallet_balance_repository: WalletBalanceRepository

    def __init__(self) -> None:
        self._user_address = WalletAddress(USER_ADDRESS)
        self._target_address = WalletAddress(TARGET_ADDRESS)
        self._trade_size_strategy_type = TradeSizeStrategyType(TRADE_SIZE_STRATEGY)

    def get_trading_resource(self) -> TraderResource:
        trade_factory: TradeFactory = TradeFactory(
            trade_size_strategy=create_trade_size_strategy(self._trade_size_strategy_type)
        )

        trader_app_service: TraderAppService = TraderAppService(
            self._trade_repository,
            self._wallet_balance_repository,
            trade_factory
        )

        return TraderResource(
            self._user_address,
            self._target_address,
            trader_app_service
        )