from List.extended_list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.list_integers = IntegerList(5, 6, 7)

    def test_init_create_all_attributes(self):
        list_integers = IntegerList(5, 6, 7)
        self.assertEqual([5, 6, 7], list_integers._IntegerList__data)

    def test_init_takes_not_integers(self):
        list_integers = IntegerList(5.6, '6', 7.2)
        self.assertEqual([], list_integers._IntegerList__data)

    def test_add_integer_is_added(self):
        result = self.list_integers.add(100)
        self.assertEqual([5, 6, 7, 100], result)

    def test_add_none_integers_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integers.add(5.3)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_return_index_remove_element(self):
        el = self.list_integers.remove_index(0)
        self.assertEqual(5, el)
        self.assertEqual([6, 7], self.list_integers._IntegerList__data)

    def test_return_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_with_valid_index_return_element(self):
        el = self.list_integers.remove_index(0)
        self.assertEqual(5, el)
        self.assertEqual([6, 7], self.list_integers._IntegerList__data)

    def test_with_not_valid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_element_at_index(self):
        self.list_integers.insert(0, 100)
        self.assertEqual([100, 5, 6, 7], self.list_integers._IntegerList__data)

    def test_insert_none_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integers.insert(0, 5.3)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_integer_non_valid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.insert(4, 100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_biggest_from_list(self):
        res = self.list_integers.get_biggest()
        self.assertEqual(7, res)

    def test_get_index(self):
        index = self.list_integers.get_index(5)
        self.assertEqual(0, index)


if __name__ == "__main__":
    main()
