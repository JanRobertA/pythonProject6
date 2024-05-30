#Oppgavesett 2 Oppgave 2

class Animal:

    def make_sound(self):
        print("Some generic sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):

    def make_sound(self):
        print("Meow!")


animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()


cat = Cat()
cat.make_sound()
