
a=3
b=7
c=a
a=b
b=c
print(a)
print(b)

# without using 3rd variable.

a = 5
b = 7
a = a + b
b = a - b
a = a - b
print(a)
print(b)