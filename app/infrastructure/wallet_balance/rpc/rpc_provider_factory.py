from app.config.env import INFURA_API_KEY, ALCHEMY_PRIVATE_KEY
from app.interfaces.exceptions.no_rpc_found_exception import NoRpcFoundException
from app.infrastructure.wallet_balance.rpc.rpc_provider import RpcProvider


def create_rpc_provider() -> RpcProvider[float]:
    rpc_urls: list[str] = []

    if INFURA_API_KEY:
        rpc_urls.append("https://polygon-mainnet.infura.io/v3/" + INFURA_API_KEY)
    if ALCHEMY_PRIVATE_KEY:
        rpc_urls.append("https://polygon-mainnet.g.alchemy.com/v2/" + ALCHEMY_PRIVATE_KEY)
    if len(rpc_urls) == 0:
        raise NoRpcFoundException()

    return RpcProvider(rpc_urls, timeout=5)