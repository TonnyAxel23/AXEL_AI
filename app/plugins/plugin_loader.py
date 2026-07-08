import importlib
import inspect
import pkgutil

from app.plugins.plugin_interface import PluginInterface


class PluginLoader:
    """
    Discovers and loads all AXEL plugins.
    """

    def __init__(self, container):

        self.container = container
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

                        # Resolve dependencies
                        dependencies = []

                        for service_name in obj.dependencies:

                            dependency = self.container.get(service_name)

                            if dependency is None:
                                raise RuntimeError(
                                    f"Service '{service_name}' required by "
                                    f"{obj.__name__} is not registered."
                                )

                            dependencies.append(dependency)

                        # Create plugin
                        plugin = obj(*dependencies)

                        # Support one or many intents
                        intents = plugin.intent

                        if not isinstance(intents, (list, tuple, set)):
                            intents = [intents]

                        for intent in intents:
                            self._plugins[intent] = plugin

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