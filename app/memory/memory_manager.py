from app.memory.short_term import ShortTermMemory
from app.memory.long_term import LongTermMemory


class MemoryManager:

    """
    Central memory interface for AXEL.
    """

    def __init__(self):

        self.short_term = ShortTermMemory()

        self.long_term = LongTermMemory()

    def remember(
            self,
            key: str,
            value: str,
            persistent: bool = True
    ):

        if persistent:

            self.long_term.remember(
                key,
                value
            )

        else:

            self.short_term.remember(
                key,
                value
            )

    def recall(
            self,
            key: str
    ):

        value = self.short_term.recall(key)

        if value is not None:

            return value

        return self.long_term.recall(key)

    def get_memory_item(
            self,
            key: str
    ):
        return self.long_term.get_item(key)

    def forget(
            self,
            key: str
    ):

        self.long_term.forget(key)

    def all(self):

        return self.long_term.all()