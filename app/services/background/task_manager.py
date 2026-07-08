from app.services.background.task import BackgroundTask


class TaskManager:
    """
    Manages all AXEL background services.
    """

    def __init__(self):

        self._tasks = {}

    def register(self, task: BackgroundTask):

        self._tasks[task.name] = task

    def start(self, name: str):

        task = self._tasks.get(name)

        if task:

            task.start()

    def stop(self, name: str):

        task = self._tasks.get(name)

        if task:

            task.stop()

            task.join()

    def start_all(self):

        for task in self._tasks.values():

            task.start()

    def stop_all(self):

        for task in self._tasks.values():

            task.stop()

        for task in self._tasks.values():

            task.join()

    def get(self, name: str):

        return self._tasks.get(name)

    def all_tasks(self):

        return self._tasks