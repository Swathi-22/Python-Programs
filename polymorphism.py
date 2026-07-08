# poly - many
# morph - forms

# operator overloading

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,oth):
        return self.m1 + oth.m1 , self.m2 + oth.m2
    
    def __sub__(self,oth):
        return self.m1 - self.m2 , oth.m1 - oth.m2
    

s1 = Student(8,10)
s2 = Student(7,9)

print(s1 + s2)
print(s1 - s2)

# here __add__ is the class for + operator , and __sub__ indicates - operator