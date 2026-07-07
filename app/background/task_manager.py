from app.background.background_task import BackgroundTask


class TaskManager:
    """
    Responsible for managing every background task.
    """

    def __init__(self) -> None:
        self._tasks: dict[str, BackgroundTask] = {}

    def register(self, task: BackgroundTask) -> None:
        self._tasks[task.name] = task

    def start(self, name: str) -> None:
        task = self._tasks.get(name)

        if task:
            task.start()

    def stop(self, name: str) -> None:
        task = self._tasks.get(name)

        if task:
            task.stop()

    def start_all(self) -> None:
        for task in self._tasks.values():
            task.start()

    def stop_all(self) -> None:
        for task in self._tasks.values():
            task.stop()

        for task in self._tasks.values():
            task.join()

    def get(self, name: str):
        return self._tasks.get(name)

    def all_tasks(self):
        return self._tasks