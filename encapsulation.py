class Student:

    def __init__(self,m1,m2,m3):
        self.m1 = m1  #public
        self._m2 = m2 #protected
        self.__m3 = m3  #private

    def __add__(self,oth):
        return self.m1 + oth.m1 , self._m2 + oth._m2 , self.__m3 + oth.__m3
    
    # def __sub__(self,oth):
    #     return self.m1 - self._m2 , oth.m1 - oth.m2 , self.__m3 - oth.m3
    
s1 = Student(8,10,4)
s2 = Student(7,9,7)

print(s1 + s2 )
# print(s1 - s2)