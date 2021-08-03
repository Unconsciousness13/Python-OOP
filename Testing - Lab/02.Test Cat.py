import unittest


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTest(unittest.TestCase):
    def setUp(self) -> None:
        self.kitty = Cat('Cezar')

    def test_init_data(self):
        self.assertEqual("Cezar", self.kitty.name)
        self.assertFalse(self.kitty.fed)
        self.assertFalse(self.kitty.sleepy)
        self.assertEqual(0, self.kitty.size)

    def test_cat_size_increase_after_eating(self):
        self.assertEqual(0, self.kitty.size)
        self.kitty.eat()
        self.assertEqual(1, self.kitty.size)

    def test_cat_feed_after_eating(self):
        self.assertFalse(self.kitty.fed)
        self.kitty.eat()
        self.assertTrue(self.kitty.fed)

    def test_cannot_eat_if_already_feed_raise(self):
        self.assertFalse(self.kitty.fed)
        self.kitty.eat()
        self.assertTrue(self.kitty.fed)

        with self.assertRaises(Exception) as ex:
            self.kitty.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cant_sleep_if_not_fed_raise(self):
        self.assertFalse(self.kitty.fed)
        with self.assertRaises(Exception) as ex:
            self.kitty.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.assertFalse(self.kitty.sleepy)
        self.kitty.eat()
        self.assertTrue(self.kitty.sleepy)
        self.kitty.sleep()
        self.assertFalse(self.kitty.sleepy)


if __name__ == "__main__":
    unittest.main()
