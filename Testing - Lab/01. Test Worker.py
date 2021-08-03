class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Test', 100, 10)

    def test_worker_init(self):
        self.assertEqual('Test', self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_increase_after_rest_method_called(self):
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_if_worker_try_to_work_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_worker_money_increase_after_work(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(100, self.worker.money)

    def test_if_worker_energy_decrease_after_work(self):
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

    def test_if_get_info_return_prop_string(self):
        actual_result = self.worker.get_info()
        exp_result = 'Test has saved 0 money.'

        self.assertEqual(exp_result, actual_result)


if __name__ == "__main__":
    unittest.main()
