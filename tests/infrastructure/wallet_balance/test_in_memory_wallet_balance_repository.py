"""Tests for InMemoryWalletBalanceRepository."""
import pytest
from app.domain.wallet_address import WalletAddress
from app.infrastructure.wallet_balance.in_memory_wallet_balance_repository import InMemoryWalletBalanceRepository


class TestInMemoryWalletBalanceRepository:
    """Test cases for InMemoryWalletBalanceRepository."""

    def test_get_wallet_balance_by_address_user(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test getting balance for user address."""
        repository = InMemoryWalletBalanceRepository(sample_wallet_address, sample_target_wallet_address)
        
        balance = repository.get_wallet_balance_by_address(sample_wallet_address)
        
        assert balance == 1000.0

    def test_get_wallet_balance_by_address_target(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test getting balance for target address."""
        repository = InMemoryWalletBalanceRepository(sample_wallet_address, sample_target_wallet_address)
        
        balance = repository.get_wallet_balance_by_address(sample_target_wallet_address)
        
        assert balance == 5000.0

    def test_get_wallet_balance_by_unknown_address_returns_zero(self, sample_wallet_address: WalletAddress, sample_target_wallet_address: WalletAddress) -> None:
        """Test getting balance for unknown address returns zero."""
        repository = InMemoryWalletBalanceRepository(sample_wallet_address, sample_target_wallet_address)
        unknown_address = WalletAddress("0x9999999999999999999999999999999999999999")
        
        balance = repository.get_wallet_balance_by_address(unknown_address)
        
        assert balance == 0.0
