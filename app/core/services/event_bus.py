from collections import defaultdict
from typing import Callable, Dict, List


class EventBus:
    """
    Central communication hub for AXEL.
    Components publish events and subscribe
    to events without depending on each other.
    """

    def __init__(self):

        self._listeners: Dict[str, List[Callable]] = defaultdict(list)

    from typing import Callable

    def subscribe(self, event_name: str, callback: Callable) -> None:

        self._listeners[event_name].append(callback)

    from typing import Any

    def publish(self, event_name: str, data: Any = None) -> None:

        listeners = self._listeners.get(event_name, [])

        for listener in listeners:
            listener(data)