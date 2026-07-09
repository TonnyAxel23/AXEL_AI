from app.automation.app_launcher import AppLauncher
from app.automation.browser import Browser
from app.tools.datetime_tool import DateTimeTool


class CommandProcessor:

    def process(self, command: str):

        command = command.lower().strip()

        if command == "open chrome":

            success = AppLauncher.open_app("chrome")

            return "Opening Chrome..." if success else "Chrome not found."

        elif command == "open pycharm":

            success = AppLauncher.open_app("pycharm")

            return "Opening PyCharm..." if success else "PyCharm not found."

        elif command == "open github":

            Browser.open_github()

            return "Opening GitHub..."

        elif command == "open youtube":

            Browser.open_youtube()

            return "Opening YouTube..."

        elif command == "what time is it":

            return f"The time is {DateTimeTool.current_time()}"

        elif command == "what is today's date":

            return DateTimeTool.current_date()

        else:

            return "Sorry, I don't understand that command."
