from app.core.startup import StartupManager
from app.core.assistant import Assistant


def bootstrap() -> None:
    """
    Boot the AXEL application.

    Initializes all core services,
    creates the assistant,
    and starts the main interaction loop.
    """

    # Initialize the application
    startup = StartupManager()
    container = startup.initialize()

    task_manager = container.get("task_manager")

    task_manager.start_all()

    scheduler = container.get("scheduler")

    scheduler.start()

    # Retrieve services
    ai_engine = container.get("ai_engine")

    # Create assistant
    assistant = Assistant(ai_engine)

    try:
        assistant.run()
    finally:
        scheduler.stop()
        task_manager.stop_all()

    # Start AXEL
    assistant.run()