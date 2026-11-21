"""Greedy solution for the unweighted Activity Selection problem."""

from dataclasses import dataclass
from collections.abc import Iterable


@dataclass(frozen=True, slots=True)
class Activity:
    """An activity represented by a half-open interval [start, finish)."""

    name: str
    start: int
    finish: int

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Activity name cannot be empty.")
        if isinstance(self.start, bool) or not isinstance(self.start, int):
            raise TypeError("Activity start must be an integer.")
        if isinstance(self.finish, bool) or not isinstance(self.finish, int):
            raise TypeError("Activity finish must be an integer.")
        if self.start >= self.finish:
            raise ValueError("Activity must satisfy start < finish.")


def select_activities(activities: Iterable[Activity]) -> list[Activity]:
    """Return a maximum-cardinality compatible set using earliest-finish Greedy.

    Time complexity: O(n log n), due to sorting.
    Auxiliary space: O(n), for the sorted copy and returned selection.
    If activities arrive already sorted by finish time, the selection scan
    itself takes O(n) time.
    """
    items = list(activities)
    if any(not isinstance(item, Activity) for item in items):
        raise TypeError("All elements must be Activity instances.")

    # The secondary keys make output deterministic when finish times tie.
    ordered = sorted(items, key=lambda activity: (
        activity.finish,
        activity.start,
        activity.name,
    ))

    selected: list[Activity] = []
    last_finish: int | None = None

    for activity in ordered:
        if last_finish is None or activity.start >= last_finish:
            selected.append(activity)
            last_finish = activity.finish

    return selected


def is_compatible_selection(activities: Iterable[Activity]) -> bool:
    """Check whether the supplied activities can be performed without overlap."""
    items = list(activities)
    if any(not isinstance(item, Activity) for item in items):
        raise TypeError("All elements must be Activity instances.")

    ordered = sorted(items, key=lambda activity: (
        activity.start,
        activity.finish,
        activity.name,
    ))
    return all(
        previous.finish <= current.start
        for previous, current in zip(ordered, ordered[1:])
    )
