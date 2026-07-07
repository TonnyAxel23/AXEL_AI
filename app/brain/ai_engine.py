from app.brain.commands.text_cleaner import TextCleaner
from app.brain.commands.tokenizer import Tokenizer
from app.brain.commands.intent_detector import IntentDetector
from app.brain.commands.entity_extractor import EntityExtractor
from app.brain.commands.command_registry import CommandRegistry
from app.brain.context_manager import ContextManager


class AIEngine:

    def __init__(self):

        self.intent_detector = IntentDetector()
        self.registry = CommandRegistry()
        self.context = ContextManager()

    def process(self, command: str) -> str:

        cleaned = TextCleaner.clean(command)

        words = Tokenizer.tokenize(cleaned)

        intent = self.intent_detector.detect(cleaned)

        entities = EntityExtractor.extract(words)

        if intent.name == "GET_TIME":
            entities["request"] = "time"

        elif intent.name == "GET_DATE":
            entities["request"] = "date"

        self.context.update(intent, entities)

        skill = self.registry.get_skill(intent)

        if skill:
            return skill.execute(entities)

        return "Sorry, I don't know how to do that yet."