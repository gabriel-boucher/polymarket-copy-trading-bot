"""Tests for WalletAddress domain entity."""
import pytest
from app.domain.wallet_address import WalletAddress


class TestWalletAddress:
    """Test cases for WalletAddress entity."""

    def test_wallet_address_creation(self) -> None:
        """Test creating a wallet address."""
        address_str = "0x1234567890123456789012345678901234567890"
        wallet_address = WalletAddress(address_str)

        assert str(wallet_address) == address_str

    def test_wallet_address_to_web3(self) -> None:
        """Test converting wallet address to Web3 checksum address."""
        address_str = "0x1234567890123456789012345678901234567890"
        wallet_address = WalletAddress(address_str)
        checksum_address = wallet_address.to_web3()

        assert isinstance(checksum_address, str)
        assert checksum_address.startswith("0x")
        # Web3.to_checksum_address should return a checksummed address
        assert checksum_address.lower() == address_str.lower()

    def test_wallet_address_equality(self) -> None:
        """Test that two wallet addresses with the same value are equal."""
        address_str = "0x1234567890123456789012345678901234567890"
        wallet_address1 = WalletAddress(address_str)
        wallet_address2 = WalletAddress(address_str)

        assert wallet_address1 == wallet_address2

    def test_wallet_address_inequality(self) -> None:
        """Test that two wallet addresses with different values are not equal."""
        address1 = WalletAddress("0x1234567890123456789012345678901234567890")
        address2 = WalletAddress("0x9876543210987654321098765432109876543210")

        assert address1 != address2

    def test_wallet_address_hash(self) -> None:
        """Test that wallet address can be used as dictionary key."""
        address_str = "0x1234567890123456789012345678901234567890"
        wallet_address1 = WalletAddress(address_str)
        wallet_address2 = WalletAddress(address_str)

        dictionary = {wallet_address1: "value"}
        assert wallet_address2 in dictionary
        assert dictionary[wallet_address2] == "value"
