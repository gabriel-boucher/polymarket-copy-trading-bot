def to_wallet_balance_domain(raw_balance: int, decimals: int) -> float:
    balance: float = raw_balance / (10 ** decimals)
    return balance