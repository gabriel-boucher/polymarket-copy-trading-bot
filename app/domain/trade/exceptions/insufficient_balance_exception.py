from app.domain.wallet_address import WalletAddress


class InsufficientBalanceException(Exception):
    def __init__(self, trade_size: float, wallet_address: WalletAddress) -> None:
        super().__init__(f"Insufficient balance for a trade size of {trade_size} in wallet {str(wallet_address)}")