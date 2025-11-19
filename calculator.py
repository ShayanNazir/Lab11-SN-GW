#https://github.com/ShayanNazir/Lab11-SN-GW
#Partner 1: Shayan Nazir
#Partner 2: Gordon Whitcomb

import math



def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b



def mul(a, b):
    return multiply(a, b)


def divide(a, b):
    """
    divide(a, b) should return b / a
    and raise ZeroDivisionError if a == 0
    """
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (a == 0).")
    return b / a



def div(a, b):
    return divide(a, b)




def logarithm(a, b):
    """
    log_a(b)  →  logarithm base a of b

    Must raise ValueError if:
    - a <= 0 or a == 1   (invalid base)
    - b <= 0            (invalid argument)
    """
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Log argument must be positive.")
    return math.log(b, a)


def exponent(a, b):
    """Return a raised to the power b."""
    return a ** b



def exp(a, b):
    return exponent(a, b)


# ------------------ Extra math functions ------------------ #

def hypotenuse(a, b):
    """
    Return the length of the hypotenuse given legs a and b.
    """
    return math.hypot(a, b)


def square_root(x):
    """
    Return square root of x.
    Raise ValueError if x is negative.
    """
    if x < 0:
        raise ValueError("square_root() not defined for negative numbers.")
    return math.sqrt(x)




