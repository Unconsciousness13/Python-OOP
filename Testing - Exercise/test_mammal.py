from project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    KINGDOM = "animals"

    def setUp(self) -> None:
        self.mammal = Mammal("Cezar", "Dogs", "Waw")

    def test_init_properties(self):
        self.assertEqual("Cezar", self.mammal.name)
        self.assertEqual("Dogs", self.mammal.type)
        self.assertEqual("Waw", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_animal_make_sound(self):
        result = "Cezar makes Waw"
        self.assertEqual(result, self.mammal.make_sound())

    def test_get_info(self):
        result = "Cezar is of type Dogs"
        self.assertEqual(result, self.mammal.info())

    def test_the_kingdom(self):
        result = "animals"
        self.assertEqual(result, self.mammal.get_kingdom())


if __name__ == "__main__":
    unittest.main()
