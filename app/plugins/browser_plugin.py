from app.plugins.plugin_interface import PluginInterface
from app.brain.commands.intents import Intent
from app.automation.browser import Browser


class BrowserPlugin(PluginInterface):

    @property
    def metadata(self):
        return {
            "name": "Browser Plugin",
            "version": "1.0.0",
            "author": "Tonny Odhiambo",
            "intent": Intent.OPEN_WEBSITE,
            "description": "Open websites in the default browser."
        }

    def execute(self, entities: dict) -> str:

        website = entities.get("website")

        if not website:
            return "Which website should I open?"

        website = website.lower()

        if website == "github":
            Browser.open_github()
            return "Opening GitHub..."

        if website == "google":
            Browser.open_google()
            return "Opening Google..."

        if website == "youtube":
            Browser.open_youtube()
            return "Opening YouTube..."

        return f"I don't know how to open '{website}'."