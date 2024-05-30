#oppgavesett 2 oppgave 1

class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")



person = Person("Alice", 30)
person.introduce()

student = Student("Bob", 20, "S12345")
student.introduce()
student.study()
