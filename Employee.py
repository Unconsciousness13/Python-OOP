class Employee:

    def __init__(self,id: int, firts_name: str, last_name: str, salary: int):
        self.id = id
        self.first_name = firts_name
        self.last_name = last_name
        self.salary = salary
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    def raise_salary(self,raised: int):
        self.salary += raised  
        return self.salary
    def get_annual_salary(self):
        return self.salary * 12




employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
