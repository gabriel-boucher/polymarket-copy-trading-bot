"""Pytest configuration and shared fixtures."""
import pytest
from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.trade import Trade
from app.domain.wallet_address import WalletAddress


@pytest.fixture
def sample_wallet_address() -> WalletAddress:
    """Create a sample wallet address for testing."""
    return WalletAddress("0x1234567890123456789012345678901234567890")


@pytest.fixture
def sample_target_wallet_address() -> WalletAddress:
    """Create a sample target wallet address for testing."""
    return WalletAddress("0x9876543210987654321098765432109876543210")


@pytest.fixture
def sample_trade(sample_wallet_address: WalletAddress) -> Trade:
    """Create a sample trade for testing."""
    return Trade(
        token_id=TokenId("token123"),
        price=0.5,
        size=10.0,
        side=SideType.BUY,
        wallet_address=sample_wallet_address,
        condition_id=ConditionId("condition123"),
        outcome="YES",
        timestamp=1234567890,
    )


@pytest.fixture
def sample_trade_sell(sample_wallet_address: WalletAddress) -> Trade:
    """Create a sample SELL trade for testing."""
    return Trade(
        token_id=TokenId("token456"),
        price=0.7,
        size=5.0,
        side=SideType.SELL,
        wallet_address=sample_wallet_address,
        condition_id=ConditionId("condition456"),
        outcome="NO",
        timestamp=1234567891,
    )
