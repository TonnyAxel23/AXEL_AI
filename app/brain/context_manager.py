class ContextManager:

    def __init__(self):

        self.last_intent = None

        self.last_entities = {}

    def update(self, intent, entities: dict) -> None:

        self.last_intent = intent

        self.last_entities = entities

    def get_context(self) -> dict:

        return {

            "intent": self.last_intent,

            "entities": self.last_entities

        }
