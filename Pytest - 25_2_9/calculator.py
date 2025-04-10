import math
import sqlite3

def add(a, b):
    return a + b  # + 0.1 # 0.99999999999


# 0.4444444444 + 0.66666666666
# 0.999999999999
# 1.0

def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def make_error():
    raise IndexError()

def make_value_error(ex):
    print(ex)
    raise ValueError

def create_table(query):
    # check if table exists
    raise sqlite3.IntegrityError

def say_hello():
    name = input("enter name? ")
    return f"hello {name}"

def power(num: int, power_of: int):
    result = num
    for _ in range(1, power_of):
        result *= num
    return result

def sqrt(num):
    return math.sqrt(num)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result