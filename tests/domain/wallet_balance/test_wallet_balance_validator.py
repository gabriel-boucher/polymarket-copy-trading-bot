"""Tests for WalletBalanceValidator."""
import pytest
from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.exceptions.no_wallet_balance_found_exception import NoWalletBalanceFoundException
from app.domain.wallet_balance.wallet_balance_validator import WalletBalanceValidator


class TestWalletBalanceValidator:
    """Test cases for WalletBalanceValidator."""

    def test_validate_wallet_balance_success(self, sample_wallet_address: WalletAddress) -> None:
        """Test validating a valid wallet balance."""
        balance = 100.0
        WalletBalanceValidator.validate_wallet_balance(balance, sample_wallet_address)
        # Should not raise any exception

    def test_validate_wallet_balance_zero_success(self, sample_wallet_address: WalletAddress) -> None:
        """Test that zero balance is valid."""
        balance = 0.0
        WalletBalanceValidator.validate_wallet_balance(balance, sample_wallet_address)
        # Should not raise any exception

    def test_validate_wallet_balance_none_raises_exception(self, sample_wallet_address: WalletAddress) -> None:
        """Test that None balance raises NoWalletBalanceFoundException."""
        with pytest.raises(NoWalletBalanceFoundException) as exc_info:
            WalletBalanceValidator.validate_wallet_balance(None, sample_wallet_address)  # type: ignore[arg-type]
        
        assert str(sample_wallet_address) in str(exc_info.value)
