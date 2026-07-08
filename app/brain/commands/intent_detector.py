from .intents import Intent


class IntentDetector:

    OPEN_WORDS = [

        "open",

        "launch",

        "run",

        "start"

    ]

    TIME_WORDS = [

        "time",

        "clock"

    ]

    DATE_WORDS = [

        "date",

        "today"

    ]

    def detect(self, command):

        text = command.lower()

        if any(word in text for word in self.OPEN_WORDS):

            if "github" in text:

                return Intent.OPEN_WEBSITE

            return Intent.OPEN_APP

        if any(word in text for word in self.TIME_WORDS):

            return Intent.GET_TIME

        if any(word in text for word in self.DATE_WORDS):

            return Intent.GET_DATE

        if command.startswith("remember"):
            return Intent.REMEMBER

        if command.startswith("what is my"):
            return Intent.RECALL

        if command.startswith("who is my"):
            return Intent.RECALL

        if command.startswith("forget"):
            return Intent.FORGET

        return Intent.UNKNOWN