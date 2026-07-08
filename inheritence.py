# single level inheritence

class Person1:
    def __init__(self):
        pass

    def read(self):
        print("Person can read")

    def write(self):
        print("Person can write")


class Person2(Person1):
    def __init__(self):
        pass

    def jump(self):
        print("Person can jump")

    def run(self):
        print("Person can run")


p2 = Person2()
p2.read()


# multi level

class Person1:
    def __init__(self):
        pass

    def read(self):
        print("Person can read")

    def write(self):
        print("Person can write")


class Person2(Person1):
    def __init__(self):
        pass

    def jump(self):
        print("Person can jump")

    def run(self):
        print("Person can run")


class Person3(Person2):
    def __init__(self):
        pass

    def fly(self):
        print("Person can fly")

    def swim(self):
        print("Person can swim")


class Person4(Person3):
    def __init__(self):
        pass

    def sleep(self):
        print("Person can sleep")

    def eat(self):
        print("Person can eat")

p4 = Person4()
p4.read()


# method overriding

class Person1:
    def __init__(self):
        pass

    def read(self):
        print("Person can read")

    def write(self):
        print("Person can write")

    def speak(self):
        print("Person 1 can speak")


class Person2(Person1):
    def __init__(self):
        pass

    def jump(self):
        print("Person can jump")

    def run(self):
        print("Person can run")
    
    def speak(self):
        print("Person 2 can speak")


class Person3(Person2):
    def __init__(self):
        pass

    def fly(self):
        print("Person can fly")

    def swim(self):
        print("Person can swim")
    
    def speak(self):
        print("Person 3 can speak")


class Person4(Person3):
    def __init__(self):
        pass

    def sleep(self):
        print("Person can sleep")

    def eat(self):
        print("Person can eat")
    
    def speak(self):
        print("Person 4 can speak")
        super().speak()  # super() method used to call to inherit property from immediate super class

p4 = Person4()
p4.speak()  # return person 4 can speak (method overriding)


# multiple

class Person1:
    def __init__(self):
        pass

    def read(self):
        print("Person can read")

    def write(self):
        print("Person can write")

    def speak(self):
        print("Person 1 can speak")


class Person2:
    def __init__(self):
        pass

    def jump(self):
        print("Person can jump")

    def run(self):
        print("Person can run")
    
    def speak(self):
        print("Person 2 can speak")


class Person3:
    def __init__(self):
        pass

    def fly(self):
        print("Person can fly")

    def swim(self):
        print("Person can swim")
    
    def speak(self):
        print("Person 3 can speak")


class Person4(Person2,Person1,Person3):
    def __init__(self):
        pass

    def sleep(self):
        print("Person can sleep")

    def eat(self):
        print("Person can eat")
    
    # def speak(self):
    #     print("Person 4 can speak")

    # if p4 don't have speak method it using MRO - Method Reselution Order .  Which means in Person2,Person1,Person3 Person2 got priority.
        

p4 = Person4()
p4.speak()  # return person 4 can speak (method overriding)
