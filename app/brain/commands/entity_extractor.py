class EntityExtractor:

    APPS = {

        "chrome",

        "pycharm",

        "notepad",

        "calculator"

    }

    WEBSITES = {

        "github",

        "youtube",

        "google"

    }

    @classmethod
    def extract(cls, words: list[str]) -> dict:

        entities = {}

        for word in words:

            if word in cls.APPS:

                entities["app"] = word

            if word in cls.WEBSITES:

                entities["website"] = word

        return entities