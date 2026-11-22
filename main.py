"""Demonstratii Greedy: Activity Selection si 0/1 Knapsack."""

from dataclasses import dataclass
from itertools import combinations


# Activity Selection
@dataclass(frozen=True)
class Activity:
    name: str
    start: int
    finish: int


def select_activities(activities):
    """Selecteaza numarul maxim de activitati compatibile.

    Complexitate: O(n log n) pentru sortare si O(n) pentru parcurgere.
    """
    ordered = sorted(activities, key=lambda a: (a.finish, a.start, a.name))
    selected = []
    last_finish = None

    for activity in ordered:
        if last_finish is None or activity.start >= last_finish:
            selected.append(activity)
            last_finish = activity.finish

    return selected


def is_compatible_selection(activities):
    ordered = sorted(activities, key=lambda a: (a.start, a.finish))
    return all(
        previous.finish <= current.start
        for previous, current in zip(ordered, ordered[1:])
    )


# 0/1 Knapsack: exemplu in care euristica Greedy nu gaseste optimul
@dataclass(frozen=True)
class Item:
    name: str
    weight: int
    value: int


def greedy_by_value_density(items, capacity):
    """Alege obiectele dupa raportul valoare/greutate.

    Euristica nu garanteaza optimul pentru problema 0/1 Knapsack.
    """
    ordered = sorted(
        items,
        key=lambda item: (-item.value / item.weight, item.weight, item.name),
    )
    chosen = []
    used_weight = 0

    for item in ordered:
        if used_weight + item.weight <= capacity:
            chosen.append(item)
            used_weight += item.weight

    return chosen


def optimal_by_bruteforce(items, capacity):
    """Cauta solutia exacta prin enumerarea submultimilor (doar pentru exemple mici)."""
    best = []
    best_value = 0
    best_weight = 0

    for size in range(len(items) + 1):
        for subset in combinations(items, size):
            weight = total_weight(subset)
            value = total_value(subset)
            if weight <= capacity and (
                value > best_value
                or (value == best_value and weight < best_weight)
            ):
                best = list(subset)
                best_value = value
                best_weight = weight

    return best


def total_weight(items):
    return sum(item.weight for item in items)


def total_value(items):
    return sum(item.value for item in items)
