from project.vehicle import Vehicle
import unittest

DEFAULT_FUEL_CONSUMPTION = 1.25


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 177)

    def test_initial_attributes(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(177, self.vehicle.horse_power)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_successful(self):
        self.vehicle.drive(20)
        self.assertEqual(75, self.vehicle.fuel)

    def test_drive_unsuccessful(self):
        with self.assertRaises(Exception) as ex:
            result = "Not enough fuel"
            self.vehicle.drive(82)
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(result, str(ex.exception))

    def test_refuel_successful(self):
        self.vehicle.drive(50)
        self.vehicle.refuel(30)
        self.assertEqual(67.5, self.vehicle.fuel)

    def test_refuel_too_much_fuel(self):
        self.vehicle.drive(50)
        with self.assertRaises(Exception) as ex:
            result = "Too much fuel"
            self.vehicle.refuel(80)
        self.assertEqual(result, str(ex.exception))
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_str_print(self):
        result = "The vehicle has 177 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, self.vehicle.__str__())


if __name__ == "__main__":
    unittest.main()
