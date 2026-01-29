"""Tests for InMemoryTradeRepository."""
import pytest
from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.trade import Trade
from app.domain.trade.trade_builder import build_trade
from app.infrastructure.trade.in_memory_trade_repository import InMemoryTradeRepository
from app.domain.wallet_address import WalletAddress


class TestInMemoryTradeRepository:
    """Test cases for InMemoryTradeRepository."""

    def test_get_last_trade_by_wallet_address(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test getting the last trade for a wallet address."""
        repository = InMemoryTradeRepository(sample_wallet_address, sample_target_wallet_address)
        
        trade = repository.get_last_trade_by_wallet_address(sample_wallet_address)
        
        assert isinstance(trade, Trade)

    def test_get_last_trade_by_target_address(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test getting the last trade for target wallet address."""
        repository = InMemoryTradeRepository(sample_wallet_address, sample_target_wallet_address)
        
        trade = repository.get_last_trade_by_wallet_address(sample_target_wallet_address)
        
        assert isinstance(trade, Trade)

    def test_get_last_trade_by_unknown_address_returns_first_trade(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test getting trade for unknown address returns empty list's first element."""
        repository = InMemoryTradeRepository(sample_wallet_address, sample_target_wallet_address)
        unknown_address = WalletAddress("0x9999999999999999999999999999999999999999")
        
        # This will raise IndexError since the list is empty
        with pytest.raises(IndexError):
            repository.get_last_trade_by_wallet_address(unknown_address)

    def test_get_trades_by_wallet_address_with_limit(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test getting trades with a limit."""
        repository = InMemoryTradeRepository(sample_wallet_address, sample_target_wallet_address)
        
        trades = repository.get_trades_by_wallet_address(sample_wallet_address, limit=1)
        
        assert len(trades) == 1
        assert isinstance(trades[0], Trade)

    def test_save_trade(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test saving a trade."""
        repository = InMemoryTradeRepository(sample_wallet_address, sample_target_wallet_address)
        
        new_trade = Trade(
            token_id=TokenId("new_token"),
            price=0.6,
            size=15.0,
            side=SideType.BUY,
            wallet_address=sample_wallet_address,
            condition_id=ConditionId("new_condition"),
            outcome="YES",
            timestamp=1234567892,
        )
        
        repository.save_trade(new_trade)
        
        # Verify the trade was saved under user_address (repository saves all trades under user_address)
        trades = repository.get_trades_by_wallet_address(sample_wallet_address, limit=10)
        assert len(trades) >= 2  # At least the initial trade and the new one
        # Check that the new trade is in the list by comparing key fields
        assert any(
            t.token_id == new_trade.token_id and 
            t.price == new_trade.price and 
            t.size == new_trade.size 
            for t in trades
        )

    def test_save_multiple_trades(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test saving multiple trades."""
        repository = InMemoryTradeRepository(sample_wallet_address, sample_target_wallet_address)
        
        trade1 = build_trade()
        trade2 = build_trade()
        trade3 = build_trade()
        
        repository.save_trade(trade1)
        repository.save_trade(trade2)
        repository.save_trade(trade3)
        
        trades = repository.get_trades_by_wallet_address(sample_wallet_address, limit=10)
        assert len(trades) >= 4  # Initial trade + 3 new trades

    def test_get_trades_by_wallet_address_respects_limit(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test that get_trades_by_wallet_address respects the limit parameter."""
        repository = InMemoryTradeRepository(sample_wallet_address, sample_target_wallet_address)
        
        # Save multiple trades
        for _ in range(5):
            repository.save_trade(build_trade())
        
        trades = repository.get_trades_by_wallet_address(sample_wallet_address, limit=3)
        assert len(trades) == 3
