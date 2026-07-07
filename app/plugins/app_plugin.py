from app.plugins.plugin_interface import PluginInterface
from app.brain.commands.intents import Intent
from app.automation.app_launcher import AppLauncher


class AppPlugin(PluginInterface):

    @property
    def intent(self):
        return Intent.OPEN_APP

    def execute(self, entities: dict) -> str:

        app = entities.get("app")

        if not app:
            return "Which application should I open?"

        if AppLauncher.open_app(app):
            return f"Opening {app.title()}..."

        return f"I couldn't find {app}."