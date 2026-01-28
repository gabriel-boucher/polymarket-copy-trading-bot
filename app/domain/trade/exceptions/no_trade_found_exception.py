from app.domain.wallet_address import WalletAddress


class NoTradeFoundException(Exception):
    def __init__(self, wallet_address: WalletAddress) -> None:
        super().__init__(f"No trade found for the wallet {str(wallet_address)}")