from project.pet_shop import PetShop

import unittest


class TestPetShop(unittest.TestCase):
    def setUp(self) -> None:
        self.ps = PetShop("Spas")

    def test_init(self):
        self.assertEqual("Spas", self.ps.name)
        self.assertEqual({}, self.ps.food)
        self.assertEqual([], self.ps.pets)

    def test_add_food_quantity_raise(self):
        quantity = -1
        with self.assertRaises(Exception) as ex:
            self.ps.add_food("kukruz", quantity)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_correct_quantity(self):
        quantity = 100
        name = "kukuruz"
        self.assertEqual({}, self.ps.food)
        self.ps.add_food(name, quantity)
        self.assertEqual(f"Successfully added {quantity:.2f} grams of {name}.", self.ps.add_food(name, quantity))

    def test_add_pet_correct(self):
        name = "Spas"
        self.assertEqual([], self.ps.pets)
        self.assertEqual(f"Successfully added {name}.", self.ps.add_pet(name))

    def test_pet_raise_same_name(self):
        name = "Spas"
        self.assertEqual([], self.ps.pets)
        self.ps.add_pet(name)
        with self.assertRaises(Exception) as ex:
            self.ps.add_pet(name)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_if_not_in_pets_raise(self):
        food = "food"
        name = "Spas"
        self.assertEqual([], self.ps.pets)
        self.assertEqual({}, self.ps.food)
        self.ps.add_pet("Krika")
        self.ps.add_food(food, 200)
        with self.assertRaises(Exception) as ex:
            self.ps.feed_pet(food, name)
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_if_food_not_in_foods(self):
        messsage = 'You do not have qdeniee'
        self.ps.add_pet("Spas")
        self.ps.add_food("qdene", 200)
        self.ps.add_food("qdenie", 200)
        self.assertEqual(messsage, self.ps.feed_pet("qdeniee", "Spas"))
        self.assertEqual(200, self.ps.food["qdene"])

    def test_adding_food_if_low_than_100(self):
        name = "Spas"
        food = "food"
        self.ps.add_food(food, 99)
        self.ps.add_pet(name)
        self.assertEqual("Adding food...", self.ps.feed_pet(food, name))
        self.assertEqual(1099, self.ps.food[food])

    def test_feeding_if_all_food_is_more_than_100(self):
        food = "ala"
        name = "Spas"
        self.ps.add_pet(name)
        self.ps.add_food(food, 101)
        self.assertEqual(f"{name} was successfully fed", self.ps.feed_pet(food, name))
        self.assertEqual(1, self.ps.food[food])

    def test_string_output(self):
        name = f'Shop {self.ps.name}:\n' \
               f'Pets: {", ".join(self.ps.pets)}'
        self.assertEqual(name, self.ps.__repr__())


if __name__ == "__main__":
    unittest.main()
