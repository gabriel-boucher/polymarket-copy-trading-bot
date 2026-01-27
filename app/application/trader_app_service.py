from app.domain.trade.trade import Trade
from app.domain.wallet_address import WalletAddress
from app.domain.trade.trade_factory import TradeFactory
from app.domain.wallet_balance.wallet_balance_repository import WalletBalanceRepository
from app.domain.trade.trade_repository import TradeRepository


class TraderAppService:
    __trade_repository: TradeRepository
    __wallet_balance_repository: WalletBalanceRepository
    __trade_factory: TradeFactory

    def __init__(self, trade_repository: TradeRepository, wallet_balance_repository: WalletBalanceRepository, trade_factory: TradeFactory) -> None:
        self.__trade_repository = trade_repository
        self.__wallet_balance_repository = wallet_balance_repository
        self.__trade_factory = trade_factory

    def place_trade(self, user_address: WalletAddress, target_address: WalletAddress) -> None:
        target_trade: Trade = self.__trade_repository.get_last_trade_by_wallet_address(target_address)
        if target_trade is None:
            raise ValueError("No trade found for the target address")

        user_balance: float = self.__wallet_balance_repository.get_wallet_balance_by_address(user_address)
        if user_balance is None:
            raise ValueError("Could not fetch user balance")

        target_balance: float = self.__wallet_balance_repository.get_wallet_balance_by_address(target_address)
        if target_balance is None:
            raise ValueError("Could not fetch target balance")

        user_trade = self.__trade_factory.create_trade(target_trade, user_balance, target_balance)
        print(user_trade)

        self.__trade_repository.save_trade(user_trade)
