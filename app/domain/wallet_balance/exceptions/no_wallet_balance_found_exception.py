from app.domain.wallet_address import WalletAddress


class NoWalletBalanceFoundException(Exception):
    def __init__(self, wallet_address: WalletAddress) -> None:
        super().__init__(f"No wallet balance found for the wallet {str(wallet_address)}")