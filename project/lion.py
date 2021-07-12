from project.animal import Animal
MONEY_FOR_CARE = 50
class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, 50)
        

        