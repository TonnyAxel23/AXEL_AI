import heapq
import threading
import time
from datetime import datetime, timedelta

from app.services.background.scheduled_task import ScheduledTask


class Scheduler:

    def __init__(self):

        self._queue = []

        self._task_index = {}

        self._lock = threading.Lock()

        self._running = False

        self._thread = None

    def schedule(self, task: ScheduledTask) -> str:

        with self._lock:
            task.cancelled = False

            heapq.heappush(
                self._queue,
                task
            )


            self._task_index[task.id] = task

            return task.id

    def cancel(self, task_id: str) -> bool:

        with self._lock:
            task = self._task_index.get(task_id)

            if task:
                task.cancelled = True

                return True

        return False

    def start(self):

        if self._running:
            return

        self._running = True

        self._thread = threading.Thread(

            target=self.run,

            daemon=True,

            name="Scheduler"

        )

        self._thread.start()

    def get_task(self, task_id: str):

        return self._task_index.get(task_id)

    def list_tasks(self):

        return list(self._task_index.values())

    def list_tasks(self):

        return list(self._task_index.values())

    def stop(self):

        self._running = False

        if self._thread:

            self._thread.join()

    def run(self):

        while self._running:

            now = datetime.now()

            with self._lock:

                while self._queue:

                    task = self._queue[0]

                    if task.cancelled:

                        heapq.heappop(self._queue)

                        continue

                    if task.execute_at > now:

                        break

                    heapq.heappop(self._queue)

                    try:

                        task.callback()
                        self._task_index.pop(
                            task.id,
                            None
                        )

                    except Exception as e:

                        print(e)

                    if task.recurring:

                        task.execute_at = (

                            datetime.now()

                            + timedelta(

                                seconds=task.interval

                            )

                        )

                        heapq.heappush(

                            self._queue,

                            task

                        )

            time.sleep(0.5)