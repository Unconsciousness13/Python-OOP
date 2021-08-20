from project.people.child import Child
from project.rooms.room import Room
import unittest


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room("Test", 100, 2)

    def test_init(self):
        self.assertEqual("Test", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_raise(self):
        with self.assertRaises(Exception) as ex:
            self.room.expenses -= 1
        return self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_correct_expenses(self):
        self.room.expenses = 1
        self.assertEqual(1, self.room.expenses)

    def test_correct_expenses_calculate(self):
        self.assertEqual(0, self.room.expenses)
        roko = Child(2, 2, 10)
        exp = 420
        self.room.calculate_expenses([roko])
        self.assertEqual(exp, self.room.expenses)


if __name__ == "__main__":
    unittest.main()
