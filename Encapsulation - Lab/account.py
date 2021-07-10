class Account:
    def __init__(self, id , balance , pin) -> None:
        self.__id = id
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin):
        if not pin == self.__pin:
            return "Wrong pin"

        return self.__id
    
    def change_pin(self, old_pin , new_pin):
        if not old_pin == self.__pin:
            return "Wrong pin"

        self.__pin = new_pin
        return "Pin changed" 




account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
