class NoRpcFoundException(Exception):
    def __init__(self) -> None:
        super().__init__("No RPC endpoint found.")