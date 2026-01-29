"""Tests for TradeFactory."""
import pytest
from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.trade import Trade
from app.domain.trade.trade_factory import TradeFactory
from app.domain.trade.trade_size_strategy.fixed_trade_size_strategy import FixedTradeSizeStrategy
from app.domain.trade.trade_size_strategy.proportional_trade_size_strategy import ProportionalTradeSizeStrategy
from app.domain.trade.trade_size_strategy.target_trade_size_strategy import TargetTradeSizeStrategy
from app.domain.wallet_address import WalletAddress


class TestTradeFactory:
    """Test cases for TradeFactory."""

    def test_create_trade_with_fixed_strategy(self, sample_trade: Trade) -> None:
        """Test creating a trade with fixed size strategy."""
        fixed_size = 5.0
        strategy = FixedTradeSizeStrategy(fixed_size)
        factory = TradeFactory(strategy)
        
        user_balance = 100.0
        target_balance = 50.0
        
        user_trade = factory.create_trade(sample_trade, user_balance, target_balance)
        
        assert user_trade.token_id == sample_trade.token_id
        assert user_trade.price == sample_trade.price
        assert user_trade.size == fixed_size
        assert user_trade.side == sample_trade.side
        assert user_trade.wallet_address == sample_trade.wallet_address
        assert user_trade.condition_id == sample_trade.condition_id
        assert user_trade.outcome == sample_trade.outcome
        assert user_trade.timestamp == sample_trade.timestamp

    def test_create_trade_with_proportional_strategy(self, sample_trade: Trade) -> None:
        """Test creating a trade with proportional size strategy."""
        strategy = ProportionalTradeSizeStrategy()
        factory = TradeFactory(strategy)
        
        user_balance = 100.0
        target_balance = 50.0
        # Expected size: 100 / 50 * 10 = 20.0
        expected_size = user_balance / target_balance * sample_trade.size
        
        user_trade = factory.create_trade(sample_trade, user_balance, target_balance)
        
        assert user_trade.size == expected_size
        assert user_trade.token_id == sample_trade.token_id
        assert user_trade.price == sample_trade.price
        assert user_trade.side == sample_trade.side

    def test_create_trade_with_target_strategy(self, sample_trade: Trade) -> None:
        """Test creating a trade with target size strategy."""
        strategy = TargetTradeSizeStrategy()
        factory = TradeFactory(strategy)
        
        user_balance = 100.0
        target_balance = 50.0
        
        user_trade = factory.create_trade(sample_trade, user_balance, target_balance)
        
        assert user_trade.size == sample_trade.size
        assert user_trade.token_id == sample_trade.token_id
        assert user_trade.price == sample_trade.price
        assert user_trade.side == sample_trade.side

    def test_create_trade_preserves_all_fields(self, sample_trade: Trade) -> None:
        """Test that factory preserves all trade fields except size."""
        strategy = FixedTradeSizeStrategy(5.0)
        factory = TradeFactory(strategy)
        
        user_trade = factory.create_trade(sample_trade, 100.0, 50.0)
        
        assert user_trade.token_id == sample_trade.token_id
        assert user_trade.price == sample_trade.price
        assert user_trade.side == sample_trade.side
        assert user_trade.wallet_address == sample_trade.wallet_address
        assert user_trade.condition_id == sample_trade.condition_id
        assert user_trade.outcome == sample_trade.outcome
        assert user_trade.timestamp == sample_trade.timestamp
