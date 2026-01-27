from app.config.config_factory import create_config
from app.interfaces.trader_resource import TraderResource


if __name__ == "__main__":
    config = create_config()
    tradingResource: TraderResource = config.get_trading_resource()
    tradingResource.start()