# abstraction is the mechanism which hide complex details 
# child class can't use method from parent class.
# here we want to use method makes_sound in class Dog by hiding from Animal, for that we need to use abstractmethod decorator at the top of the method.

from abc import ABC,abstractmethod


class Animal:
    def __init__(self):
        pass

    @abstractmethod
    def makes_sound(self):
        print("Animal can make sound")

    def walk(self):
        print("Animal can walk")


class Dog(Animal):
    def __init__(self):
        pass

    def makes_sound(self):
        print("Baw Baw")

d = Dog()
d.makes_sound()
d.walk()