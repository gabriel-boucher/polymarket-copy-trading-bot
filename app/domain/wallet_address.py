from dataclasses import dataclass

from web3 import Web3
from eth_typing import ChecksumAddress


@dataclass
class WalletAddress:
    __wallet_address: str

    def __str__(self) -> str:
        return self.__wallet_address

    def to_web3(self) -> ChecksumAddress:
        return Web3.to_checksum_address(self.__wallet_address)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, WalletAddress) and self.__wallet_address == other.__wallet_address

    def __hash__(self) -> int:
        return hash(self.__wallet_address)