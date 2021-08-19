import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.tp = PaintFactory("Test", 100)

    def test_init(self):
        self.assertEqual("Test", self.tp.name)
        self.assertEqual(100, self.tp.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.tp.valid_ingredients)

    def test_adding_ingredient_raise_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.tp.add_ingredient("white", 102)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_adding_correct_ingredient_adding(self):
        self.tp.add_ingredient("white", 24)
        self.assertEqual({"white": 24}, self.tp.ingredients)

    def test_adding_wrong_ingredient_raise(self):
        with self.assertRaises(Exception) as ex:
            self.tp.add_ingredient("ahite", 12)
        self.assertEqual("Ingredient of type ahite not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient_correctly(self):
        self.tp.add_ingredient("white", 24)
        self.tp.remove_ingredient("white", 12)
        self.assertEqual({"white": 12}, self.tp.ingredients)

    def test_remove_ingredient_raise_quantity_error(self):
        self.tp.add_ingredient("white", 24)
        with self.assertRaises(Exception) as ex:
            self.tp.remove_ingredient("white", 25)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_raise_key_error(self):
        self.tp.add_ingredient("white", 24)
        with self.assertRaises(Exception) as ex:
            self.tp.remove_ingredient("whita", 23)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_products_returning(self):
        self.assertEqual(0, len(self.tp.products))
