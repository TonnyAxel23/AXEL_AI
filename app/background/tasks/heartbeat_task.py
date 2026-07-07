import time

from app.background.background_task import BackgroundTask


class HeartbeatTask(BackgroundTask):
    """
    Prints a heartbeat every five seconds.

    Used to verify that the background
    task system is alive.
    """

    def __init__(self):
        super().__init__("Heartbeat")

    def run(self) -> None:

        while self.running:

            print("❤️  AXEL heartbeat...")

            time.sleep(5)