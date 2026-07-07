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

    # Retrieve services
    ai_engine = container.get("ai_engine")

    # Create assistant
    assistant = Assistant(ai_engine)

    # Start AXEL
    assistant.run()