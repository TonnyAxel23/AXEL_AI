# app/core/startup.py

from app.core.services.event_bus import EventBus
from app.core.services.service_container import ServiceContainer
from app.core.logger import logger

from app.config.settings import settings

from app.brain.ai_engine import AIEngine


class StartupManager:

    def __init__(self):

        self.container = ServiceContainer()

    def initialize(self):

        logger.info("Starting AXEL...")

        # Register configuration
        self.container.register(
            "settings",
            settings
        )

        # Register Event Bus
        self.container.register(
            "event_bus",
            EventBus()
        )

        # Register AI Engine
        self.container.register(
            "ai_engine",
            AIEngine()
        )

        logger.info("Core services initialized.")

        return self.container