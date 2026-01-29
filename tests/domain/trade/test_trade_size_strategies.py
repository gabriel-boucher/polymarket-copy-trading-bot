"""Tests for trade size strategies."""
import pytest
from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.exceptions.insufficient_balance_exception import InsufficientBalanceException
from app.domain.trade.trade import Trade
from app.domain.trade.trade_size_strategy.fixed_trade_size_strategy import FixedTradeSizeStrategy
from app.domain.trade.trade_size_strategy.proportional_trade_size_strategy import ProportionalTradeSizeStrategy
from app.domain.trade.trade_size_strategy.target_trade_size_strategy import TargetTradeSizeStrategy
from app.domain.wallet_address import WalletAddress


class TestFixedTradeSizeStrategy:
    """Test cases for FixedTradeSizeStrategy."""

    def test_calculate_size_returns_fixed_size(self, sample_trade: Trade) -> None:
        """Test that fixed strategy returns the configured fixed size."""
        fixed_size = 5.0
        strategy = FixedTradeSizeStrategy(fixed_size)
        
        result = strategy.calculate_size(sample_trade, 100.0, 50.0)
        
        assert result == fixed_size

    def test_calculate_size_insufficient_balance_raises_exception(self, sample_trade: Trade) -> None:
        """Test that insufficient balance raises InsufficientBalanceException."""
        fixed_size = 100.0
        strategy = FixedTradeSizeStrategy(fixed_size)
        user_balance = 50.0
        
        with pytest.raises(InsufficientBalanceException) as exc_info:
            strategy.calculate_size(sample_trade, user_balance, 100.0)
        
        assert str(fixed_size) in str(exc_info.value)
        assert str(sample_trade.wallet_address) in str(exc_info.value)

    def test_calculate_size_exact_balance_succeeds(self, sample_trade: Trade) -> None:
        """Test that exact balance is sufficient."""
        fixed_size = 50.0
        strategy = FixedTradeSizeStrategy(fixed_size)
        
        result = strategy.calculate_size(sample_trade, 50.0, 100.0)
        
        assert result == fixed_size


class TestProportionalTradeSizeStrategy:
    """Test cases for ProportionalTradeSizeStrategy."""

    def test_calculate_size_proportional_calculation(self, sample_trade: Trade) -> None:
        """Test proportional size calculation."""
        strategy = ProportionalTradeSizeStrategy()
        user_balance = 100.0
        target_balance = 50.0
        # Expected: 100 / 50 * 10 = 20.0
        expected_size = user_balance / target_balance * sample_trade.size
        
        result = strategy.calculate_size(sample_trade, user_balance, target_balance)
        
        assert result == expected_size

    def test_calculate_size_user_has_more_balance(self, sample_trade: Trade) -> None:
        """Test when user has more balance than target."""
        strategy = ProportionalTradeSizeStrategy()
        user_balance = 200.0
        target_balance = 100.0
        # Expected: 200 / 100 * 10 = 20.0
        expected_size = user_balance / target_balance * sample_trade.size
        
        result = strategy.calculate_size(sample_trade, user_balance, target_balance)
        
        assert result == expected_size

    def test_calculate_size_user_has_less_balance(self, sample_trade: Trade) -> None:
        """Test when user has less balance than target."""
        strategy = ProportionalTradeSizeStrategy()
        user_balance = 25.0
        target_balance = 100.0
        # Expected: 25 / 100 * 10 = 2.5
        expected_size = user_balance / target_balance * sample_trade.size
        
        result = strategy.calculate_size(sample_trade, user_balance, target_balance)
        
        assert result == expected_size

    def test_calculate_size_insufficient_balance_raises_exception(self, sample_trade: Trade) -> None:
        """Test that insufficient balance raises InsufficientBalanceException."""
        strategy = ProportionalTradeSizeStrategy()
        user_balance = 5.0
        target_balance = 10.0
        # Calculated size: 5 / 10 * 10 = 5.0, but if calculation results in > user_balance
        
        # Create a trade with large size that would exceed balance
        large_trade = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=100.0,  # Large size
            side=SideType.BUY,
            wallet_address=WalletAddress("0x123"),
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )
        
        with pytest.raises(InsufficientBalanceException):
            strategy.calculate_size(large_trade, user_balance, target_balance)


class TestTargetTradeSizeStrategy:
    """Test cases for TargetTradeSizeStrategy."""

    def test_calculate_size_returns_target_size(self, sample_trade: Trade) -> None:
        """Test that target strategy returns the target trade size."""
        strategy = TargetTradeSizeStrategy()
        
        result = strategy.calculate_size(sample_trade, 100.0, 50.0)
        
        assert result == sample_trade.size

    def test_calculate_size_insufficient_balance_raises_exception(self, sample_trade: Trade) -> None:
        """Test that insufficient balance raises InsufficientBalanceException."""
        strategy = TargetTradeSizeStrategy()
        user_balance = 5.0  # Less than trade size of 10.0
        
        with pytest.raises(InsufficientBalanceException) as exc_info:
            strategy.calculate_size(sample_trade, user_balance, 100.0)
        
        assert str(sample_trade.size) in str(exc_info.value)
        assert str(sample_trade.wallet_address) in str(exc_info.value)

    def test_calculate_size_exact_balance_succeeds(self, sample_trade: Trade) -> None:
        """Test that exact balance is sufficient."""
        strategy = TargetTradeSizeStrategy()
        
        result = strategy.calculate_size(sample_trade, sample_trade.size, 100.0)
        
        assert result == sample_trade.size
