import time

from app.application.trader_app_service import TraderAppService
from app.domain.wallet_address import WalletAddress


class TraderResource:
    __user_address: WalletAddress
    __target_address: WalletAddress
    __trading_app_service: TraderAppService

    def __init__(self, user_address: WalletAddress, target_address: WalletAddress, trading_app_service: TraderAppService) -> None:
        self.__user_address = user_address
        self.__target_address = target_address
        self.__trading_app_service = trading_app_service

    def start(self) -> None:
        while True:
            try:
                self.__trading_app_service.place_trade(self.__user_address, self.__target_address)
            except Exception as e:
                print(f"Error placing trade: {e}")
            time.sleep(1)
