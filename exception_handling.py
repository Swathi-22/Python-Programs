
try:
    a=8
    b=0
    print(a/b)
except Exception as error:
    print("An error occured",error)


# multiple exception

try:
    a=int(input("Enter a number : "))
    b=0
    print(a/b)
except ZeroDivisionError:
    print("you can't divide a number by zero")

try:
    a=int(input("Enter a number : "))
    b=6
    print(a/b)
except ValueError:
    print("check values")

try:
    a=int(input("Enter a number : "))
    b="swathi"
    print(a/b)
except TypeError:
    print("check types")


# finally
try:
    a=5
    b=0
    print(a/b)
except Exception as e:
    print("An error occured",e)
finally:
    print("this always excecute!!!!!!")


# AssertionError
age = 4
assert age > 18 , "Age have to be greater"

# raise
raise(IndentationError("My name is swathi"))

# own exception handling
class MyError(Exception):
    pass

name="mohan"
if name != "swathi":
    raise MyError("name should be swathi")
