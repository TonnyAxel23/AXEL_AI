from dataclasses import dataclass, asdict, field
from datetime import datetime
from uuid import uuid4


@dataclass
class MemoryItem:

    key: str
    value: str

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat()
    )

    updated_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat()
    )

    def to_dict(self) -> dict:

        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):

        return cls(
            key=data["key"],
            value=data["value"],
            id=data["id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )