from py_clob_client.client import ClobClient

from app.config.env import USER_PRIVATE_KEY, USER_ADDRESS


CLOB_CLIENT_HOST: str = "https://clob.polymarket.com"
CLOB_CLIENT_CHAIN_ID: int = 137
CLOB_CLIENT_SIGNATURE_TYPE: int = 2

def create_clob_client() -> ClobClient:
    client: ClobClient = ClobClient(
        host=CLOB_CLIENT_HOST,
        key=USER_PRIVATE_KEY,
        chain_id=CLOB_CLIENT_CHAIN_ID,
        signature_type=CLOB_CLIENT_SIGNATURE_TYPE,
        funder=USER_ADDRESS
    )
    client.set_api_creds(client.create_or_derive_api_creds())

    return client