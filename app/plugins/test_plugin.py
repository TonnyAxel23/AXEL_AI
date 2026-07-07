from app.plugins.plugin_interface import PluginInterface
from app.brain.commands.intents import Intent


class TestPlugin(PluginInterface):

    @property
    def metadata(self):
        return {
            "name": "Test Plugin",
            "version": "1.0.0",
            "author": "Tonny Odhiambo",
            "intent": Intent.UNKNOWN,
            "description": "Plugin used for testing."
        }

    def execute(self, entities: dict) -> str:
        return "Test plugin works!"