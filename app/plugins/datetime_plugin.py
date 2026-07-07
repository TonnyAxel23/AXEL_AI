from app.plugins.plugin_interface import PluginInterface
from app.brain.commands.intents import Intent
from app.tools.datetime_tool import DateTimeTool


class DateTimePlugin(PluginInterface):

    @property
    def metadata(self):
        return {
            "name": "DateTime Plugin",
            "version": "1.0.0",
            "author": "Tonny Odhiambo",
            "intent": Intent.GET_TIME,
            "description": "Provides the current date and time."
        }

    def execute(self, entities: dict) -> str:

        request = entities.get("request")

        if request == "time":
            return f"The current time is {DateTimeTool.current_time()}"

        if request == "date":
            return f"Today's date is {DateTimeTool.current_date()}"

        return "I couldn't determine whether you wanted the date or time."