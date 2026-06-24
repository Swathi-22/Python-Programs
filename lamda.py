import math

z=lambda x,y : x+y
print(z(4,5))

sum = lambda a,b,c,d : (a+b+c+d)/5
print(sum(4,5,6,7))

# square of a number
sqre = lambda x : x**2
print(sqre(5))

# square root of a number
# square_root = lambda y : math.sqrt(y)
square_root = lambda y : y**(0.5)
print(square_root(7))

# perimeter of a circle
# perimeter = lambda r : 2*math.pi*r
perimeter = lambda r : 2*3.14*r
print(perimeter(5))

# full name of a person
full_name = lambda first_name,last_name : first_name+" "+last_name
print(full_name("swathi","suresh"))

# check if a person eligible or not
result = lambda age : "elgible" if age >= 18 else "not eleigible"
print(result(26))