from abc import ABC, abstractmethod


class SkillInterface(ABC):

    @abstractmethod
    def execute(self, entities: dict) -> str:
        """Execute the skill."""
        pass