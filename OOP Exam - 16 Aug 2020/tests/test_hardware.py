import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software




class HardwareTests(unittest.TestCase):

    def test_init(self):
        hardware = Hardware("PakoHard", "Very_heavy", 69, 69)
        self.assertEqual("Very_heavy", hardware.type)
        self.assertEqual("PakoHard", hardware.name)
        self.assertEqual(69, hardware.memory)
        self.assertEqual(69, hardware.capacity)
        self.assertEqual([], hardware.software_components)

    def test_software_install(self):
        hardware = Hardware("PakoHard", "Heavy", 69, 69)
        software = Software("PakoVirus", "Light", 29, 29)
        hardware.install(software)
        self.assertEqual([software], hardware.software_components)

    def test_not_capacity_install_raises(self):
        software = Software("PakoVirus", "Light", 10, 10)
        hardware = Hardware("PakoHard", "Heavy", 2, 5)
        with self.assertRaises(Exception) as ex:
            hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_software_uninstall(self):
        hardware = Hardware("PakoHard", "Heavy", 69, 69)
        software = Software("PakoVirus", "Light", 29, 29)
        hardware.install(software)
        hardware.uninstall(software)
        self.assertEqual([], hardware.software_components)


if __name__ == '__main__':
    unittest.main()
