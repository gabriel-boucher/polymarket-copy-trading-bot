from app.domain.trade.trade import Trade
from app.domain.trade.trade_validator import TradeValidator
from app.domain.wallet_address import WalletAddress
from app.domain.trade.trade_factory import TradeFactory
from app.domain.wallet_balance.wallet_balance_repository import WalletBalanceRepository
from app.domain.trade.trade_repository import TradeRepository
from app.domain.wallet_balance.wallet_balance_validator import WalletBalanceValidator


class TraderAppService:
    __trade_repository: TradeRepository
    __wallet_balance_repository: WalletBalanceRepository
    __trade_factory: TradeFactory
    __trade_validator: TradeValidator
    __wallet_balance_validator: WalletBalanceValidator

    def __init__(self, trade_repository: TradeRepository, wallet_balance_repository: WalletBalanceRepository, trade_factory: TradeFactory, trade_validator: TradeValidator, wallet_balance_validator: WalletBalanceValidator) -> None:
        self.__trade_repository = trade_repository
        self.__wallet_balance_repository = wallet_balance_repository
        self.__trade_factory = trade_factory
        self.__trade_validator = trade_validator
        self.__wallet_balance_validator = wallet_balance_validator

    def place_trade(self, user_address: WalletAddress, target_address: WalletAddress) -> None:
        target_trade: Trade = self.__trade_repository.get_last_trade_by_wallet_address(target_address)
        self.__trade_validator.validate_trade(target_trade, target_address)

        user_balance: float = self.__wallet_balance_repository.get_wallet_balance_by_address(user_address)
        self.__wallet_balance_validator.validate_wallet_balance(user_balance, user_address)

        target_balance: float = self.__wallet_balance_repository.get_wallet_balance_by_address(target_address)
        self.__wallet_balance_validator.validate_wallet_balance(target_balance, target_address)

        user_trade: Trade = self.__trade_factory.create_trade(target_trade, user_balance, target_balance)
        print(user_trade)

        # self.__trade_repository.save_trade(user_trade)
