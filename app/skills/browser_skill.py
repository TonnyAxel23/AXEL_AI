from app.interfaces.skill_interface import SkillInterface
from app.automation.browser import Browser


class BrowserSkill(SkillInterface):

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

        return "I don't know that website yet."