from abc import ABC, abstractmethod
from typing import Any


class PluginInterface(ABC):
    """
    Base class for every AXEL plugin.

    Every plugin must provide metadata describing itself
    and implement an execute() method that performs its task.
    """

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
        """
        Shortcut for the plugin's display name.
        """
        return self.metadata["name"]

    @property
    def version(self) -> str:
        """
        Shortcut for the plugin version.
        """
        return self.metadata["version"]

    @property
    def author(self) -> str:
        """
        Shortcut for the plugin author.
        """
        return self.metadata["author"]

    @property
    def description(self) -> str:
        """
        Shortcut for the plugin description.
        """
        return self.metadata["description"]

    @property
    def intent(self):
        """
        Shortcut for the plugin's intent.
        """
        return self.metadata["intent"]

    @abstractmethod
    def execute(self, entities: dict) -> str:
        """
        Execute the plugin.

        Args:
            entities: Extracted entities from the user's command.

        Returns:
            A response string for the assistant.
        """
        pass