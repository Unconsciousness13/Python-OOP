from project.animal import Animal
MONEY_FOR_CARE = 60
class Cheetah(Animal):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age,60)
        