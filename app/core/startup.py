# app/core/startup.py

from app.core.services.event_bus import EventBus
from app.core.services.service_container import ServiceContainer
from app.core.logger import logger

from app.config.settings import settings

from app.plugins.plugin_loader import PluginLoader
from app.brain.ai_engine import AIEngine

from app.background.task_manager import TaskManager
from app.background.tasks.heartbeat_task import HeartbeatTask

class StartupManager:
    """
    Responsible for bootstrapping the AXEL application.

    Initializes and registers all core services
    in the Service Container.
    """

    def __init__(self) -> None:
        self.container = ServiceContainer()

    def initialize(self) -> ServiceContainer:

        logger.info("=" * 60)
        logger.info("Starting AXEL...")
        logger.info("=" * 60)

        # -----------------------------
        # Configuration
        # -----------------------------
        self.container.register(
            "settings",
            settings
        )

        # -----------------------------
        # Event Bus
        # -----------------------------
        event_bus = EventBus()

        self.container.register(
            "event_bus",
            event_bus
        )

        # -----------------------------
        # Task Manager
        # -----------------------------
        task_manager = TaskManager()

        task_manager.register(
            HeartbeatTask()
        )

        self.container.register(
            "task_manager",
            task_manager
        )

        # -----------------------------
        # Plugin Loader
        # -----------------------------
        plugin_loader = PluginLoader()
        plugin_loader.load_plugins()

        self.container.register(
            "plugin_loader",
            plugin_loader
        )

        # -----------------------------
        # AI Engine
        # -----------------------------
        ai_engine = AIEngine(plugin_loader)

        self.container.register(
            "ai_engine",
            ai_engine
        )

        logger.info(
            f"Loaded {len(plugin_loader.all_plugins())} plugins."
        )

        logger.info(
            f"Plugins Loaded: {len(plugin_loader.all_plugins())}"
        )

        logger.info(
            f"Plugins Failed: {len(plugin_loader.failed_plugins())}"
        )

        logger.info("AXEL startup completed successfully.")

        return self.container