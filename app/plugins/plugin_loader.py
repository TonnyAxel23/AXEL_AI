import importlib
import inspect
import pkgutil
import traceback

from app.plugins.plugin_interface import PluginInterface


class PluginLoader:
    """
    Automatically discovers and loads all plugins
    inside the app.plugins package.
    """

    def __init__(self) -> None:
        self._plugins = {}
        self._failed_plugins = {}

    def load_plugins(self) -> None:
        """
        Discover and load all plugins.
        """

        print("\n" + "=" * 60)
        print("Loading AXEL Plugins")
        print("=" * 60)

        package = importlib.import_module("app.plugins")

        loaded = 0
        failed = 0

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):

            if module_name in (
                "__init__",
                "plugin_loader",
                "plugin_interface",
            ):
                continue

            try:

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

                        loaded += 1

                        print(
                            f"✓ {plugin.name} "
                            f"(v{plugin.version})"
                        )

            except Exception as e:

                failed += 1

                self._failed_plugins[module_name] = str(e)

                print(f"✗ {module_name}")
                print(f"    {e}")

                # Uncomment while debugging
                # traceback.print_exc()

        print("-" * 60)
        print(f"Loaded : {loaded}")
        print(f"Failed : {failed}")
        print("=" * 60)

    def get(self, intent):
        return self._plugins.get(intent)

    def all_plugins(self) -> dict:
        return self._plugins

    def failed_plugins(self) -> dict:
        return self._failed_plugins