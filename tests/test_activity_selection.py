import unittest

from greedy_project.activity_selection import (
    Activity,
    is_compatible_selection,
    select_activities,
)


class ActivitySelectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.activities = [
            Activity("A", 1, 4),
            Activity("B", 3, 5),
            Activity("C", 0, 6),
            Activity("D", 5, 7),
            Activity("E", 8, 9),
            Activity("F", 5, 9),
        ]

    def test_classroom_example(self) -> None:
        selected = select_activities(self.activities)
        self.assertEqual([activity.name for activity in selected], ["A", "D", "E"])

    def test_result_is_compatible(self) -> None:
        selected = select_activities(self.activities)
        self.assertTrue(is_compatible_selection(selected))

    def test_adjacent_activities_are_compatible(self) -> None:
        selected = select_activities([
            Activity("B", 3, 5),
            Activity("A", 1, 3),
        ])
        self.assertEqual([activity.name for activity in selected], ["A", "B"])

    def test_unsorted_input_is_supported(self) -> None:
        selected = select_activities(reversed(self.activities))
        self.assertEqual([activity.name for activity in selected], ["A", "D", "E"])

    def test_empty_input(self) -> None:
        self.assertEqual(select_activities([]), [])

    def test_single_activity(self) -> None:
        activity = Activity("A", 2, 5)
        self.assertEqual(select_activities([activity]), [activity])

    def test_invalid_interval(self) -> None:
        with self.assertRaises(ValueError):
            Activity("invalid", 4, 4)

    def test_non_activity_input(self) -> None:
        with self.assertRaises(TypeError):
            select_activities(["not an activity"])  # type: ignore[list-item]


if __name__ == "__main__":
    unittest.main()
