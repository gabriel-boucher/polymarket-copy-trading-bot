import os

import dotenv

dotenv.load_dotenv()

# Application Settings
APP_START_TYPE: str = os.getenv("APP_START_TYPE", "in_memory")  # Options: "in_memory", "rpc"

# Addresses
USER_ADDRESS: str = os.getenv("USER_ADDRESS", "")
TARGET_ADDRESS: str = os.getenv("TARGET_ADDRESS", "")

# User Credentials
USER_PRIVATE_KEY: str = os.getenv("USER_PRIVATE_KEY", "")

# Trade Configuration
TRADE_SIZE_STRATEGY: str = os.getenv("TRADE_SIZE_STRATEGY", "fixed")  # Options: "fixed", "proportional", "same_as_target"
FIXED_TRADE_SIZE: float = float(os.getenv("FIXED_TRADE_SIZE", "5.0"))

# RPC Credentials
INFURA_API_KEY: str = os.getenv("INFURA_API_KEY", "")
ALCHEMY_PRIVATE_KEY: str = os.getenv("ALCHEMY_PRIVATE_KEY", "")
