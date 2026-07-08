from app.plugins.plugin_interface import PluginInterface
from app.brain.commands.intents import Intent
from app.brain.commands.memory_parser import MemoryParser


class MemoryPlugin(PluginInterface):
    """
    Handles persistent conversational memory.
    """

    dependencies = ["memory"]

    def __init__(self, memory_manager):
        self.memory = memory_manager

    @property
    def metadata(self):
        return {
            "name": "Memory Plugin",
            "version": "1.0.0",
            "author": "Tonny Odhiambo",
            "intent": [
                Intent.REMEMBER,
                Intent.RECALL,
                Intent.FORGET
            ],
            "description": "Persistent memory support.",
            "enabled": True,
            "category": "AI"
        }

    def execute(self, entities: dict) -> str:

        command = entities["command"]
        intent = entities["intent"]

        if intent == Intent.REMEMBER:

            parsed = MemoryParser.parse_remember(command)

            if not parsed:
                return "I couldn't understand what to remember."

            key, value = parsed

            self.memory.remember(key, value)

            return f"I'll remember that your {key} is {value}."

        if intent == Intent.RECALL:

            key = MemoryParser.parse_recall(command)

            if not key:
                return "I couldn't understand what you want me to recall."

            value = self.memory.recall(key)

            if value:
                return f"Your {key} is {value}."

            return f"I don't know your {key} yet."

        if intent == Intent.FORGET:

            key = MemoryParser.parse_forget(command)

            if not key:
                return "I couldn't understand what you want me to forget."

            self.memory.forget(key)

            return f"I've forgotten your {key}."

        return "Unsupported memory request."