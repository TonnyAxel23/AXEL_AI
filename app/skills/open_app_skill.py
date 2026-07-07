from app.interfaces.skill_interface import SkillInterface
from app.automation.app_launcher import AppLauncher


class OpenAppSkill(SkillInterface):

    def execute(self, entities: dict) -> str:

        app = entities.get("app")

        if not app:
            return "Which application would you like me to open?"

        success = AppLauncher.open_app(app)

        if success:
            return f"Opening {app.title()}..."

        return f"I couldn't find {app}."