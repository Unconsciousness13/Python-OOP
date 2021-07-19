from abc import abstractmethod, abstractproperty, ABC


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, fuel: int):
        pass

    @abstractmethod
    def refuel(self, distance: int):
        pass


class Car(Vehicle):
    _CONSUMPTION_PER_KM = 0.9

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self._CONSUMPTION_PER_KM)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    _CONSUMPTION_PER_KM = 1.6

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self._CONSUMPTION_PER_KM)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

