from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PartyEmployee(Employee):
    def __init__(self, name, hourly_pay, hour_work):
        super().__init__(name)
        self.hourly_pay = hourly_pay
        self.hour_work = hour_work

    def calculate_salary(self):
        return self.hourly_pay * self.hour_work


full_time_emp = FullTimeEmployee("Alice", 5000)
part_time_emp = PartyEmployee("Bob", 1500, 20)

print(f'{full_time_emp.name} Salary: {full_time_emp.calculate_salary()}')
print(f'{part_time_emp.name} Salary: {part_time_emp.calculate_salary()}')


