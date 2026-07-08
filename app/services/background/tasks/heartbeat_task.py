import time

from app.services.background.task import BackgroundTask


class HeartbeatTask(BackgroundTask):

    def __init__(self):

        super().__init__("Heartbeat")

    def run(self):

        while self.running:

            print("💙 AXEL is alive...")

            time.sleep(5)