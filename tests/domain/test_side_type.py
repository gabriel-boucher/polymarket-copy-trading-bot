"""Tests for SideType enum."""
import pytest
from app.domain.side_type import SideType


class TestSideType:
    """Test cases for SideType enum."""

    def test_side_type_buy(self) -> None:
        """Test BUY side type."""
        assert SideType.BUY.value == "BUY"

    def test_side_type_sell(self) -> None:
        """Test SELL side type."""
        assert SideType.SELL.value == "SELL"

    def test_side_type_none(self) -> None:
        """Test NONE side type."""
        assert SideType.NONE.value == ""

    def test_side_type_comparison(self) -> None:
        """Test side type comparison."""
        assert SideType.BUY == SideType.BUY
        assert SideType.SELL == SideType.SELL
        assert SideType.BUY != SideType.SELL
