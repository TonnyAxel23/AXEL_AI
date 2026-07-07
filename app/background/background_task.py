from abc import ABC, abstractmethod
import threading


class BackgroundTask(ABC):
    """
    Base class for all background tasks.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._thread: threading.Thread | None = None
        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    def start(self) -> None:
        """
        Start the task.
        """
        if self._running:
            return

        self._running = True

        self._thread = threading.Thread(
            target=self.run,
            daemon=True,
            name=self.name
        )

        self._thread.start()

    def stop(self) -> None:
        """
        Request the task to stop.
        """
        self._running = False

    def join(self, timeout: float | None = None) -> None:
        """
        Wait for the thread to finish.
        """
        if self._thread:
            self._thread.join(timeout)

    @abstractmethod
    def run(self) -> None:
        """
        Main execution loop.
        """
        raise NotImplementedError