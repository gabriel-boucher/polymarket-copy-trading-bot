from web3 import Web3

from app.config.env import INFURA_API_KEY

POLYGON_RPC_URL: str = "https://polygon-mainnet.infura.io/v3/"

def create_polygon_web3() -> Web3:
    polygon_web3: Web3 = Web3(
        Web3.HTTPProvider(POLYGON_RPC_URL + INFURA_API_KEY)
    )

    return polygon_web3