from app.interfaces.skill_interface import SkillInterface
from app.tools.datetime_tool import DateTimeTool


class DateTimeSkill(SkillInterface):

    def execute(self, entities: dict) -> str:

        request = entities.get("request")

        if request == "time":
            return f"The current time is {DateTimeTool.current_time()}"

        if request == "date":
            return f"Today is {DateTimeTool.current_date()}"

        return "I couldn't determine what date or time information you wanted."