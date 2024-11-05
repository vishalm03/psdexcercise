import math

def sin(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.sin(math.radians(x)) #dhbafb

def cos(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.cos(math.radians(x))

def tan(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.tan(math.radians(x))

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < 0:
        raise ValueError("Math domain error")
    return math.sqrt(x)

def log(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x <= 0:
        raise ValueError("Math domain error")
    return math.log(x)

def exp(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.exp(x)
