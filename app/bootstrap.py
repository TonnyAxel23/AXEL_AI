from app.core.startup import StartupManager
from app.core.services.service_names import (
    TASK_MANAGER,
    SCHEDULER,
)


def bootstrap():
    """
    Initialize AXEL and return the Service Container.

    This function should NOT start the assistant.
    It only builds the application.
    """

    startup = StartupManager()

    container = startup.initialize()

    task_manager = container.get(TASK_MANAGER)
    task_manager.start_all()

    scheduler = container.get(SCHEDULER)
    scheduler.start()

    return container
