class Vehicle:
    def __init__(self, mileage: int, max_speed: int = 150) -> None:
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
