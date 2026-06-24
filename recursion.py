# recursion

def countdown(n):
    print(n)
    if n == 0:
        return
    return countdown(n-1)

countdown(10)

# sum of upto a number
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(sum(10))

# factorial of a number
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(10))