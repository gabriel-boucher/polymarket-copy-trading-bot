from dataclasses import dataclass


@dataclass
class ConditionId:
    condition_id: str

    def __str__(self) -> str:
        return self.condition_id