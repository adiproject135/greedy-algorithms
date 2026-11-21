"""A small counterexample for the 0/1 Knapsack density heuristic.

The greedy function is intentionally a heuristic, not an exact 0/1 Knapsack
solver. The brute-force function is included only for tiny teaching examples.
"""

from dataclasses import dataclass
from itertools import combinations
from collections.abc import Iterable


@dataclass(frozen=True, slots=True)
class Item:
    """An indivisible item in a 0/1 Knapsack instance."""

    name: str
    weight: int
    value: int

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Item name cannot be empty.")
        if isinstance(self.weight, bool) or not isinstance(self.weight, int):
            raise TypeError("Item weight must be an integer.")
        if isinstance(self.value, bool) or not isinstance(self.value, int):
            raise TypeError("Item value must be an integer.")
        if self.weight <= 0:
            raise ValueError("Item weight must be positive.")
        if self.value < 0:
            raise ValueError("Item value cannot be negative.")


def _validate(items: Iterable[Item], capacity: int) -> list[Item]:
    if isinstance(capacity, bool) or not isinstance(capacity, int):
        raise TypeError("Capacity must be an integer.")
    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")

    materialized = list(items)
    if any(not isinstance(item, Item) for item in materialized):
        raise TypeError("All elements must be Item instances.")
    return materialized


def greedy_by_value_density(items: Iterable[Item], capacity: int) -> list[Item]:
    """Choose fitting items by descending value/weight ratio.

    This is optimal for the *fractional* Knapsack problem, but not in general
    for 0/1 Knapsack, where each item must be taken whole or not at all.
    """
    available = _validate(items, capacity)
    ordered = sorted(
        available,
        key=lambda item: (-item.value / item.weight, item.weight, item.name),
    )

    chosen: list[Item] = []
    used_weight = 0
    for item in ordered:
        if used_weight + item.weight <= capacity:
            chosen.append(item)
            used_weight += item.weight
    return chosen


def optimal_by_bruteforce(items: Iterable[Item], capacity: int) -> list[Item]:
    """Find an exact optimum by enumerating subsets (exponential time).

    This function is appropriate only for very small examples; it is used
    here as a transparent reference result for the classroom counterexample.
    """
    available = _validate(items, capacity)
    best: tuple[Item, ...] = ()
    best_value = 0
    best_weight = 0

    for size in range(len(available) + 1):
        for subset in combinations(available, size):
            weight = total_weight(subset)
            value = total_value(subset)
            if weight <= capacity and (
                value > best_value
                or (value == best_value and weight < best_weight)
            ):
                best = subset
                best_value = value
                best_weight = weight

    return list(best)


def total_weight(items: Iterable[Item]) -> int:
    return sum(item.weight for item in items)


def total_value(items: Iterable[Item]) -> int:
    return sum(item.value for item in items)
