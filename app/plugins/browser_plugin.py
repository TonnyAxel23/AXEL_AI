from app.plugins.plugin_interface import PluginInterface
from app.brain.commands.intents import Intent
from app.automation.browser import Browser


class BrowserPlugin(PluginInterface):

    @property
    def intent(self):
        return Intent.OPEN_WEBSITE

    def execute(self, entities: dict) -> str:

        website = entities.get("website")

        if website == "github":
            Browser.open_github()
            return "Opening GitHub..."

        if website == "youtube":
            Browser.open_youtube()
            return "Opening YouTube..."

        if website == "google":
            Browser.open_google()
            return "Opening Google..."

        return "Unknown website."