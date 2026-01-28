from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.exceptions.no_wallet_balance_found_exception import NoWalletBalanceFoundException


class WalletBalanceValidator:
    @staticmethod
    def validate_wallet_balance(wallet_balance: float, wallet_address: WalletAddress) -> None:
        if wallet_balance is None:
            raise NoWalletBalanceFoundException(wallet_address)