from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker
from project.animal import Animal
class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: str, price: int):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__workers_capacity > len(self.animals) and price > self.__budget:
            return "Not enough budget"
        if self.__workers_capacity > len(self.animals):
            return "Not enough space for animal"

    def hire_worker(self, worker: str):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for i, work in enumerate(self.workers):
            if work.name == worker_name:
                self.workers.pop(i)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        for worker_ in self.workers:
            if self.__budget < worker_.salary:
                return 'You have no budget to pay your workers. They are unhappy'
            self.__budget -= worker_.salary
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        for animal_ in self.animals:
            if self.__budget < animal_.money_for_care:
                return "You have no budget to tend the animals. They are unhappy."
            self.__budget -= animal_.money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        message = []
        empty_space = '\n'

        message.append(f'You have {len(self.animals)} animals')

        lions = [a for a in self.animals if isinstance(a, Lion)]
        if lions:
            message.append(f'----- {len(lions)} Lions:')
            for l in lions:
                message.append(repr(l))

        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        if tigers:
            message.append(f'----- {len(tigers)} Tigers:')
            for t in tigers:
                message.append(repr(t))

        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]
        if cheetahs:
            message.append(f'----- {len(cheetahs)} Cheetahs:')
            for c in cheetahs:
                message.append(repr(c))

        return empty_space.join(message)

    def workers_status(self):
        message = []
        empty_space = '\n'

        message.append(f'You have {len(self.workers)} workers')

        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        if keepers:
            message.append(f'----- {len(keepers)} Keepers:')
            for k in keepers:
                message.append(repr(k))

        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        if caretakers:
            message.append(f'----- {len(caretakers)} Caretakers:')
            for c in caretakers:
                message.append(repr(c))

        vets = [w for w in self.workers if isinstance(w, Vet)]
        if vets:
            message.append(f'----- {len(caretakers)} Vets:')
            for v in vets:
                message.append(repr(v))

        return empty_space.join(message)
        
