from abc import ABC, abstractmethod


class PluginInterface(ABC):
    """
    Base class for every AXEL plugin.
    """

    @property
    @abstractmethod
    def intent(self):
        pass

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def execute(self, entities: dict) -> str:
        pass