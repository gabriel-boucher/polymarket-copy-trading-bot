from app.domain.wallet_address import WalletAddress


class IdenticalTradeException(Exception):
    def __init__(self, wallet_address: WalletAddress) -> None:
        super().__init__(f"Trade from {str(wallet_address)} is identical to the previous one")