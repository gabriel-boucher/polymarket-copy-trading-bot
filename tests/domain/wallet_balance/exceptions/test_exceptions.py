"""Tests for wallet balance exceptions."""
import pytest
from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.exceptions.no_wallet_balance_found_exception import NoWalletBalanceFoundException


class TestNoWalletBalanceFoundException:
    """Test cases for NoWalletBalanceFoundException."""

    def test_exception_message(self, sample_wallet_address: WalletAddress) -> None:
        """Test that exception message includes wallet address."""
        exception = NoWalletBalanceFoundException(sample_wallet_address)
        
        assert str(sample_wallet_address) in str(exception)
        assert "no wallet balance found" in str(exception).lower()
