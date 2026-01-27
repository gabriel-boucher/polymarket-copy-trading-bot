from dataclasses import dataclass


@dataclass
class TokenId:
    token_id: str

    def __str__(self) -> str:
        return self.token_id