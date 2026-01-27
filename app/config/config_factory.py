from app.config.config import Config
from app.config.env import APP_START_TYPE
from app.config.in_memory_config import InMemoryConfig
from app.config.polymarket_config import PolymarketConfig


def create_config() -> Config:
    if APP_START_TYPE == "in_memory":
        return InMemoryConfig()
    else:
        return PolymarketConfig()