from app.brain.commands.text_cleaner import TextCleaner
from app.brain.commands.tokenizer import Tokenizer
from app.brain.commands.intent_detector import IntentDetector
from app.brain.commands.entity_extractor import EntityExtractor
from app.brain.context_manager import ContextManager


class AIEngine:
    """
    Central processing engine for AXEL.

    Responsible for:
    - Cleaning user input
    - Detecting intent
    - Extracting entities
    - Maintaining conversation context
    - Delegating execution to plugins
    """

    def __init__(self, plugin_loader):

        self.loader = plugin_loader
        self.intent_detector = IntentDetector()
        self.context = ContextManager()

    def process(self, command: str) -> str:
        """
        Process a user command and return a response.
        """

        # Clean input
        cleaned = TextCleaner.clean(command)

        # Tokenize
        words = Tokenizer.tokenize(cleaned)

        # Detect intent
        intent = self.intent_detector.detect(cleaned)

        # Extract entities
        entities = EntityExtractor.extract(words)

        # Provide common information to every plugin
        entities["command"] = cleaned
        entities["intent"] = intent

        # Convenience fields
        if intent.name == "GET_TIME":
            entities["request"] = "time"

        elif intent.name == "GET_DATE":
            entities["request"] = "date"

        # Save conversation context
        self.context.update(intent, entities)

        # Find matching plugin
        plugin = self.loader.get(intent)

        if plugin:
            return plugin.execute(entities)

        return "Sorry, I don't know how to do that yet."