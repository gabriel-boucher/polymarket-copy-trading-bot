from app.domain.trade.exceptions.identical_trade_exception import IdenticalTradeException
from app.domain.trade.exceptions.no_trade_found_exception import NoTradeFoundException
from app.domain.trade.trade import Trade
from app.domain.wallet_address import WalletAddress


class TradeValidator:
    __previous_trade: Trade | None

    def __init__(self) -> None:
        self.__previous_trade = None

    def validate_trade(self, trade: Trade, wallet_address: WalletAddress) -> None:
        if trade is None:
            raise NoTradeFoundException(wallet_address)

        if trade == self.__previous_trade:
            raise IdenticalTradeException(wallet_address)

        self.__previous_trade = trade