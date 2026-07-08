from dataclasses import dataclass, field
from datetime import datetime
from typing import Callable
from itertools import count
from uuid import uuid4

_counter = count()


@dataclass(order=True)
class ScheduledTask:
    """
    Represents a scheduled task.

    Tasks are ordered by execution time,
    then by insertion order.

    Every task has a globally unique ID.
    """

    # ---------- Used for heap ordering ----------
    execute_at: datetime

    # ---------- User data ----------
    name: str = field(compare=False)
    callback: Callable = field(compare=False)

    # ---------- Internal ----------
    priority: int = field(
        init=False,
        default_factory=lambda: next(_counter)
    )

    id: str = field(
        init=False,
        default_factory=lambda: str(uuid4()),
        compare=False
    )

    recurring: bool = field(
        default=False,
        compare=False
    )

    interval: int | None = field(
        default=None,
        compare=False
    )

    cancelled: bool = field(
        default=False,
        compare=False
    )