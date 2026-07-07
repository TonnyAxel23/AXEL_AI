from typing import Any


class ServiceContainer:
    """
    Stores and provides shared services
    used throughout the AXEL application.
    """

    def __init__(self):
        self._services = {}

    def register(self, name: str, service: Any) -> None:
        """
        Register a service by name.
        """
        self._services[name] = service

    from typing import Any

    def get(self, name: str) -> Any:
        """
        Retrieve a registered service.
        """
        if name not in self._services:
            raise KeyError(f"Service '{name}' is not registered.")

        return self._services[name]

    def remove(self, name: str) -> None:
        """
        Check whether a service is registered.
        """
        return name in self._services

    def remove(self, name: str):
        """
        Remove a registered service.
        """
        if name in self._services:
            del self._services[name]

    def clear(self) -> None:
        """
        Remove all registered services.
        """
        self._services.clear()