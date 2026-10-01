import math


def power(base, exponent):
    return base ** exponent


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)


def nth_root(x, n):
    if n == 0:
        raise ValueError("Root degree cannot be zero")

    return x ** (1 / n)