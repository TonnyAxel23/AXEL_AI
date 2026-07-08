from abc import ABC, abstractmethod
from typing import Any


class PluginInterface(ABC):
    """
    Base class for every AXEL plugin.

    Every plugin must provide metadata describing itself
    and implement an execute() method that performs its task.
    """

    # Services required by the plugin.
    # Child plugins can override this.
    dependencies: list[str] = []

    @property
    @abstractmethod
    def metadata(self) -> dict[str, Any]:
        """
        Return plugin metadata.

        Example:
        {
            "name": "Browser Plugin",
            "version": "1.0.0",
            "author": "Tonny Odhiambo",
            "intent": Intent.OPEN_WEBSITE,
            "description": "Open websites in the default browser."
        }
        """
        pass

    @property
    def name(self) -> str:
        return self.metadata["name"]

    @property
    def version(self) -> str:
        return self.metadata["version"]

    @property
    def author(self) -> str:
        return self.metadata["author"]

    @property
    def description(self) -> str:
        return self.metadata["description"]

    @property
    def intent(self):
        return self.metadata["intent"]

    @abstractmethod
    def execute(self, entities: dict) -> str:
        """
        Execute the plugin.

        Args:
            entities: Extracted entities from the user's command.

        Returns:
            Assistant response.
        """
        pass