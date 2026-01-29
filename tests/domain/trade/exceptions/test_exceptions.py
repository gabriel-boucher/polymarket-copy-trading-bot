"""Tests for trade exceptions."""
import pytest
from app.domain.trade.exceptions.identical_trade_exception import IdenticalTradeException
from app.domain.trade.exceptions.insufficient_balance_exception import InsufficientBalanceException
from app.domain.trade.exceptions.no_trade_found_exception import NoTradeFoundException
from app.domain.wallet_address import WalletAddress


class TestIdenticalTradeException:
    """Test cases for IdenticalTradeException."""

    def test_exception_message(self, sample_wallet_address: WalletAddress) -> None:
        """Test that exception message includes wallet address."""
        exception = IdenticalTradeException(sample_wallet_address)
        
        assert str(sample_wallet_address) in str(exception)
        assert "identical" in str(exception).lower()


class TestInsufficientBalanceException:
    """Test cases for InsufficientBalanceException."""

    def test_exception_message(self, sample_wallet_address: WalletAddress) -> None:
        """Test that exception message includes trade size and wallet address."""
        trade_size = 100.0
        exception = InsufficientBalanceException(trade_size, sample_wallet_address)
        
        assert str(trade_size) in str(exception)
        assert str(sample_wallet_address) in str(exception)
        assert "insufficient" in str(exception).lower()


class TestNoTradeFoundException:
    """Test cases for NoTradeFoundException."""

    def test_exception_message(self, sample_wallet_address: WalletAddress) -> None:
        """Test that exception message includes wallet address."""
        exception = NoTradeFoundException(sample_wallet_address)
        
        assert str(sample_wallet_address) in str(exception)
        assert "no trade found" in str(exception).lower()
