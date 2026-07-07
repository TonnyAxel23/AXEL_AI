import importlib
import inspect
import pkgutil

from app.plugins.plugin_interface import PluginInterface


class PluginLoader:
    """
    Automatically discovers and loads every plugin
    inside the app.plugins package.
    """

    def __init__(self) -> None:
        self.plugins = {}

    def load_plugins(self) -> None:

        package = importlib.import_module("app.plugins")

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):

            # Skip interface and loader files
            if module_name in (
                "plugin_interface",
                "plugin_loader",
                "__init__",
            ):
                continue

            module = importlib.import_module(
                f"app.plugins.{module_name}"
            )

            for _, obj in inspect.getmembers(module, inspect.isclass):

                if (
                    issubclass(obj, PluginInterface)
                    and obj is not PluginInterface
                ):

                    plugin = obj()

                    self._plugins[plugin.intent] = plugin

                    print(f"Loaded plugin: {plugin.name}")

    def get(self, intent):

        return self._plugins.get(intent)

    def all_plugins(self) -> dict:

        return self._plugins