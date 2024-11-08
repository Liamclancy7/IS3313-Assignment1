def add_three(a, b, c):
    return a + b + c

def subtract_three(a, b, c):
    return a - b - c

def multiply_three(a, b, c):
    return a * b * c

def divide_three(a, b, c):
    # Ensure not to divide by zero; handle it as appropriate
    if b == 0 or c == 0:
        return "Error: Division by zero"
    return a / b / c

def square(a):
    return a ** 2

def cube(a):
    return a ** 3
