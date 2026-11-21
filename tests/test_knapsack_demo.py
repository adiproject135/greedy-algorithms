import unittest

from greedy_project.knapsack_demo import (
    Item,
    greedy_by_value_density,
    optimal_by_bruteforce,
    total_value,
    total_weight,
)


class KnapsackCounterexampleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.items = [
            Item("A", weight=10, value=60),
            Item("B", weight=20, value=100),
            Item("C", weight=30, value=120),
        ]

    def test_density_greedy_is_not_optimal_for_zero_one_knapsack(self) -> None:
        greedy = greedy_by_value_density(self.items, capacity=50)
        exact = optimal_by_bruteforce(self.items, capacity=50)

        self.assertEqual(total_value(greedy), 160)
        self.assertEqual(total_weight(greedy), 30)
        self.assertEqual(total_value(exact), 220)
        self.assertEqual(total_weight(exact), 50)
        self.assertEqual({item.name for item in exact}, {"B", "C"})

    def test_capacity_zero(self) -> None:
        self.assertEqual(greedy_by_value_density(self.items, 0), [])
        self.assertEqual(optimal_by_bruteforce(self.items, 0), [])

    def test_invalid_item(self) -> None:
        with self.assertRaises(ValueError):
            Item("bad", weight=0, value=10)


if __name__ == "__main__":
    unittest.main()
