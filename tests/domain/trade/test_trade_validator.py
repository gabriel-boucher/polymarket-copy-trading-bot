"""Tests for TradeValidator."""
import pytest
from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.exceptions.identical_trade_exception import IdenticalTradeException
from app.domain.trade.exceptions.no_trade_found_exception import NoTradeFoundException
from app.domain.trade.trade import Trade
from app.domain.trade.trade_validator import TradeValidator
from app.domain.wallet_address import WalletAddress


class TestTradeValidator:
    """Test cases for TradeValidator."""

    def test_validate_trade_success(self, sample_trade: Trade, sample_wallet_address: WalletAddress) -> None:
        """Test validating a valid trade."""
        validator = TradeValidator()
        validator.validate_trade(sample_trade, sample_wallet_address)
        # Should not raise any exception

    def test_validate_trade_none_raises_exception(self, sample_wallet_address: WalletAddress) -> None:
        """Test that validating None trade raises NoTradeFoundException."""
        validator = TradeValidator()
        with pytest.raises(NoTradeFoundException) as exc_info:
            validator.validate_trade(None, sample_wallet_address)  # type: ignore[arg-type]
        
        assert str(sample_wallet_address) in str(exc_info.value)

    def test_validate_identical_trade_raises_exception(
        self, sample_trade: Trade, sample_wallet_address: WalletAddress
    ) -> None:
        """Test that validating an identical trade raises IdenticalTradeException."""
        validator = TradeValidator()
        validator.validate_trade(sample_trade, sample_wallet_address)
        
        with pytest.raises(IdenticalTradeException) as exc_info:
            validator.validate_trade(sample_trade, sample_wallet_address)
        
        assert str(sample_wallet_address) in str(exc_info.value)

    def test_validate_different_trades_success(
        self, sample_trade: Trade, sample_trade_sell: Trade, sample_wallet_address: WalletAddress
    ) -> None:
        """Test that validating different trades succeeds."""
        validator = TradeValidator()
        validator.validate_trade(sample_trade, sample_wallet_address)
        validator.validate_trade(sample_trade_sell, sample_wallet_address)
        # Should not raise any exception

    def test_validate_trade_after_identical_trade_succeeds(
        self, sample_trade: Trade, sample_wallet_address: WalletAddress
    ) -> None:
        """Test that validating a different trade after an identical one succeeds."""
        validator = TradeValidator()
        validator.validate_trade(sample_trade, sample_wallet_address)
        
        # Create a different trade
        different_trade = Trade(
            token_id=TokenId("different_token"),
            price=0.6,
            size=15.0,
            side=SideType.BUY,
            wallet_address=sample_wallet_address,
            condition_id=ConditionId("different_condition"),
            outcome="NO",
            timestamp=1234567892,
        )
        
        validator.validate_trade(different_trade, sample_wallet_address)
        # Should not raise any exception
