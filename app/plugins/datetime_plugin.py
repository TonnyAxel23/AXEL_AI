from app.plugins.plugin_interface import PluginInterface
from app.brain.commands.intents import Intent
from app.tools.datetime_tool import DateTimeTool


class DateTimePlugin(PluginInterface):

    @property
    def intent(self):
        return Intent.GET_TIME

    def execute(self, entities: dict) -> str:

        request = entities.get("request")

        if request == "time":
            return f"The current time is {DateTimeTool.current_time()}"

        return f"Today's date is {DateTimeTool.current_date()}"