from app.brain.commands.intents import Intent
from app.skills.open_app_skill import OpenAppSkill
from app.skills.browser_skill import BrowserSkill
from app.skills.datetime_skill import DateTimeSkill


class CommandRegistry:

    def __init__(self):

        self.skills = {
            Intent.OPEN_APP: OpenAppSkill(),
            Intent.OPEN_WEBSITE: BrowserSkill(),
            Intent.GET_TIME: DateTimeSkill(),
            Intent.GET_DATE: DateTimeSkill()
        }

    def get_skill(self, intent):

        return self.skills.get(intent)