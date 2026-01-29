"""Tests for Trade domain entity."""
import pytest
from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.trade import Trade
from app.domain.wallet_address import WalletAddress


class TestTrade:
    """Test cases for Trade entity."""

    def test_trade_creation(self) -> None:
        """Test creating a trade with all required fields."""
        wallet_address = WalletAddress("0x1234567890123456789012345678901234567890")
        trade = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )

        assert trade.token_id.token_id == "token123"
        assert trade.price == 0.5
        assert trade.size == 10.0
        assert trade.side == SideType.BUY
        assert trade.wallet_address == wallet_address
        assert trade.condition_id.condition_id == "condition123"
        assert trade.outcome == "YES"
        assert trade.timestamp == 1234567890

    def test_trade_equality_same_trade(self) -> None:
        """Test that two trades with identical fields are equal."""
        wallet_address = WalletAddress("0x1234567890123456789012345678901234567890")
        trade1 = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )
        trade2 = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )

        assert trade1 == trade2

    def test_trade_inequality_different_token_id(self) -> None:
        """Test that trades with different token IDs are not equal."""
        wallet_address = WalletAddress("0x1234567890123456789012345678901234567890")
        trade1 = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )
        trade2 = Trade(
            token_id=TokenId("token456"),
            price=0.5,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )

        assert trade1 != trade2

    def test_trade_inequality_different_price(self) -> None:
        """Test that trades with different prices are not equal."""
        wallet_address = WalletAddress("0x1234567890123456789012345678901234567890")
        trade1 = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )
        trade2 = Trade(
            token_id=TokenId("token123"),
            price=0.6,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )

        assert trade1 != trade2

    def test_trade_inequality_different_side(self) -> None:
        """Test that trades with different sides are not equal."""
        wallet_address = WalletAddress("0x1234567890123456789012345678901234567890")
        trade1 = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )
        trade2 = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=10.0,
            side=SideType.SELL,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )

        assert trade1 != trade2

    def test_trade_inequality_with_non_trade_object(self) -> None:
        """Test that trade is not equal to a non-trade object."""
        wallet_address = WalletAddress("0x1234567890123456789012345678901234567890")
        trade = Trade(
            token_id=TokenId("token123"),
            price=0.5,
            size=10.0,
            side=SideType.BUY,
            wallet_address=wallet_address,
            condition_id=ConditionId("condition123"),
            outcome="YES",
            timestamp=1234567890,
        )

        assert trade != "not a trade"
        assert trade != 123
        assert trade != None
