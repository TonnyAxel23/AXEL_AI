from datetime import datetime

from app.memory.storage import MemoryStorage
from app.memory.memory_item import MemoryItem


class LongTermMemory:

    def __init__(self):

        self.storage = MemoryStorage()

        self.memory = self.storage.load()

    def remember(
            self,
            key: str,
            value: str
    ) -> None:

        existing = self.memory.get(key)

        if existing:

            existing["value"] = value

            existing["updated_at"] = (
                datetime.now().isoformat()
            )

        else:

            item = MemoryItem(
                key=key,
                value=value
            )

            self.memory[key] = (
                item.to_dict()
            )

        self.storage.save(
            self.memory
        )

    def recall(
            self,
            key: str
    ):

        item = self.memory.get(key)

        if not item:

            return None

        return item["value"]

    def forget(
            self,
            key: str
    ) -> None:

        if key in self.memory:

            del self.memory[key]

            self.storage.save(
                self.memory
            )

    def get_item(
            self,
            key: str
    ):

        item = self.memory.get(key)

        if item:

            return MemoryItem.from_dict(
                item
            )

        return None

    def all(self):

        return self.memory