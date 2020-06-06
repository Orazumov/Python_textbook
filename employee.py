class Employee():

    def __init__(self, name: str, surname: str, year_salary: int):
        self.name = name
        self.surname = surname
        self.year_salary = year_salary

    def give_raise(self, add: int = 5000):
        self.year_salary += add
