def inputs():
    x = int(input("Enter a number: "))
    operation = input("Enter an operation: ")
    y = int(input("Enter another number: "))
    return x, operation, y
#       mylist = [x, operation, y]

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"

    return x / y

