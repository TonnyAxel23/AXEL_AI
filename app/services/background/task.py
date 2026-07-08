from abc import ABC, abstractmethod
import threading


class BackgroundTask(ABC):
    """
    Base class for every long-running task in AXEL.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._thread: threading.Thread | None = None
        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    @property
    def thread(self) -> threading.Thread | None:
        return self._thread

    def start(self) -> None:

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
        self._running = False

    def join(self, timeout: float | None =None) -> None:

        if self._thread:

            self._thread.join(timeout)

    @abstractmethod
    def run(self) -> None:
        pass