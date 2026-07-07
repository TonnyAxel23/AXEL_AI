from app.brain.commands.text_cleaner import TextCleaner
from app.brain.commands.tokenizer import Tokenizer
from app.brain.commands.intent_detector import IntentDetector
from app.brain.commands.entity_extractor import EntityExtractor
from app.brain.context_manager import ContextManager

from app.plugins.plugin_loader import PluginLoader


class AIEngine:
    """
    The central processing engine for AXEL.
    Responsible for understanding user commands,
    extracting intent and entities, and delegating
    execution to the appropriate plugin.
    """

    def __init__(self, plugin_loader: PluginLoader) -> None:
        self.intent_detector = IntentDetector()
        self.context = ContextManager()

        # Load all available plugins
        self.loader = PluginLoader()
        self.loader.load_plugins()

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

        # Add request type for DateTime plugin
        if intent.name == "GET_TIME":
            entities["request"] = "time"

        elif intent.name == "GET_DATE":
            entities["request"] = "date"

        # Save conversation context
        self.context.update(intent, entities)

        # Find the correct plugin
        plugin = self.loader.get(intent)

        if plugin:
            return plugin.execute(entities)

        return "Sorry, I don't know how to do that yet."