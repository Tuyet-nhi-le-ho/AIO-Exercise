import math


def factorial_func(x):

    result = 1
    for i in range(1, x+1):
        result *= i
    return result


def sin(x, n):

    sin_x = 0
    for i in range(n):
        sin_x += (((-1)**i) * (x**(2*i+1))) / factorial_func(2*i+1)
    return sin_x


def cos(x, n):

    cos_x = 0
    for i in range(n):
        cos_x += (((-1)**i) * (x**(2*i)))/factorial_func(2*i)
    return cos_x


def sinh(x, n):

    sinh_x = 0
    for i in range(n):
        sinh_x += (x**(2*i+1)) / factorial_func(2*i+1)
    return sinh_x


def cosh(x, n):

    cosh_x = 0
    for i in range(n):
        cosh_x += (x**(2*i))/factorial_func(2*i)
    return cosh_x
