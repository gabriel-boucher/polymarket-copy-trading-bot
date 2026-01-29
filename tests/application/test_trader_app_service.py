"""Tests for TraderAppService."""
import pytest
from unittest.mock import Mock
from app.application.trader_app_service import TraderAppService
from app.domain.condition_id import ConditionId
from app.domain.side_type import SideType
from app.domain.token_id import TokenId
from app.domain.trade.exceptions.identical_trade_exception import IdenticalTradeException
from app.domain.trade.exceptions.no_trade_found_exception import NoTradeFoundException
from app.domain.trade.trade import Trade
from app.domain.trade.trade_factory import TradeFactory
from app.domain.trade.trade_repository import TradeRepository
from app.domain.trade.trade_size_strategy.fixed_trade_size_strategy import FixedTradeSizeStrategy
from app.domain.trade.trade_validator import TradeValidator
from app.domain.wallet_address import WalletAddress
from app.domain.wallet_balance.exceptions.no_wallet_balance_found_exception import NoWalletBalanceFoundException
from app.domain.wallet_balance.wallet_balance_repository import WalletBalanceRepository
from app.domain.wallet_balance.wallet_balance_validator import WalletBalanceValidator


class TestTraderAppService:
    """Test cases for TraderAppService."""

    @pytest.fixture
    def mock_trade_repository(self) -> Mock:
        """Create a mock trade repository."""
        return Mock(spec=TradeRepository)

    @pytest.fixture
    def mock_wallet_balance_repository(self) -> Mock:
        """Create a mock wallet balance repository."""
        return Mock(spec=WalletBalanceRepository)

    @pytest.fixture
    def trade_factory(self) -> TradeFactory:
        """Create a trade factory with fixed strategy."""
        strategy = FixedTradeSizeStrategy(5.0)
        return TradeFactory(strategy)

    @pytest.fixture
    def trade_validator(self) -> TradeValidator:
        """Create a trade validator."""
        return TradeValidator()

    @pytest.fixture
    def wallet_balance_validator(self) -> WalletBalanceValidator:
        """Create a wallet balance validator."""
        return WalletBalanceValidator()

    @pytest.fixture
    def service(
        self,
        mock_trade_repository: Mock,
        mock_wallet_balance_repository: Mock,
        trade_factory: TradeFactory,
        trade_validator: TradeValidator,
        wallet_balance_validator: WalletBalanceValidator,
    ) -> TraderAppService:
        """Create a TraderAppService instance with mocked dependencies."""
        return TraderAppService(
            trade_repository=mock_trade_repository,
            wallet_balance_repository=mock_wallet_balance_repository,
            trade_factory=trade_factory,
            trade_validator=trade_validator,
            wallet_balance_validator=wallet_balance_validator,
        )

    def test_place_trade_success(
        self,
        service: TraderAppService,
        mock_trade_repository: Mock,
        mock_wallet_balance_repository: Mock,
        sample_trade: Trade,
        sample_wallet_address: WalletAddress,
        sample_target_wallet_address: WalletAddress,
    ) -> None:
        """Test successfully placing a trade."""
        # Setup mocks
        mock_trade_repository.get_last_trade_by_wallet_address.return_value = sample_trade
        mock_wallet_balance_repository.get_wallet_balance_by_address.side_effect = [100.0, 50.0]
        
        # Execute
        service.place_trade(sample_wallet_address, sample_target_wallet_address)
        
        # Verify
        mock_trade_repository.get_last_trade_by_wallet_address.assert_called_once_with(sample_target_wallet_address)
        assert mock_wallet_balance_repository.get_wallet_balance_by_address.call_count == 2
        mock_trade_repository.save_trade.assert_called_once()

    def test_place_trade_no_trade_found_raises_exception(
        self,
        service: TraderAppService,
        mock_trade_repository: Mock,
        sample_wallet_address: WalletAddress,
        sample_target_wallet_address: WalletAddress,
    ) -> None:
        """Test that placing a trade when no trade is found raises exception."""
        mock_trade_repository.get_last_trade_by_wallet_address.return_value = None
        
        with pytest.raises(NoTradeFoundException):
            service.place_trade(sample_wallet_address, sample_target_wallet_address)

    def test_place_trade_identical_trade_raises_exception(
        self,
        service: TraderAppService,
        mock_trade_repository: Mock,
        mock_wallet_balance_repository: Mock,
        sample_trade: Trade,
        sample_wallet_address: WalletAddress,
        sample_target_wallet_address: WalletAddress,
    ) -> None:
        """Test that placing an identical trade raises exception."""
        mock_trade_repository.get_last_trade_by_wallet_address.return_value = sample_trade
        mock_wallet_balance_repository.get_wallet_balance_by_address.side_effect = [100.0, 50.0]
        
        # First call succeeds
        service.place_trade(sample_wallet_address, sample_target_wallet_address)
        
        # Second call with same trade should fail
        with pytest.raises(IdenticalTradeException):
            service.place_trade(sample_wallet_address, sample_target_wallet_address)

    def test_place_trade_no_wallet_balance_raises_exception(
        self,
        service: TraderAppService,
        mock_trade_repository: Mock,
        mock_wallet_balance_repository: Mock,
        sample_trade: Trade,
        sample_wallet_address: WalletAddress,
        sample_target_wallet_address: WalletAddress,
    ) -> None:
        """Test that placing a trade when wallet balance is None raises exception."""
        mock_trade_repository.get_last_trade_by_wallet_address.return_value = sample_trade
        mock_wallet_balance_repository.get_wallet_balance_by_address.return_value = None
        
        with pytest.raises(NoWalletBalanceFoundException):
            service.place_trade(sample_wallet_address, sample_target_wallet_address)

    def test_place_trade_creates_user_trade_with_correct_size(
        self,
        service: TraderAppService,
        mock_trade_repository: Mock,
        mock_wallet_balance_repository: Mock,
        sample_trade: Trade,
        sample_wallet_address: WalletAddress,
        sample_target_wallet_address: WalletAddress,
    ) -> None:
        """Test that the created user trade has the correct size based on strategy."""
        mock_trade_repository.get_last_trade_by_wallet_address.return_value = sample_trade
        mock_wallet_balance_repository.get_wallet_balance_by_address.side_effect = [100.0, 50.0]
        
        service.place_trade(sample_wallet_address, sample_target_wallet_address)
        
        # Verify the saved trade has the fixed size (5.0 from FixedTradeSizeStrategy)
        saved_trade = mock_trade_repository.save_trade.call_args[0][0]
        assert saved_trade.size == 5.0
        assert saved_trade.token_id == sample_trade.token_id
        assert saved_trade.price == sample_trade.price
        assert saved_trade.side == sample_trade.side
