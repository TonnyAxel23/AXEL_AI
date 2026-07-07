from app.plugins.plugin_interface import PluginInterface
from app.brain.commands.intents import Intent


class TestPlugin(PluginInterface):

    @property
    def intent(self):
        return Intent.UNKNOWN

    def execute(self, entities: dict) -> str:
        return "Test plugin works!"