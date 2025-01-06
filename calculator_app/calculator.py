# calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # sfgsafdfsdffa
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y