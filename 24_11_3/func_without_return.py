# a
from numpy.ma.extras import average


def my_ascending(x: int = 0, y: int = 0):
    result = [x, y]
    result.sort()
    print(result)


# b
def my_details(st1: str = ""):
    print(st1[0], st1[(len(st1) // 2)] ,st1[-1])


# c
def say_bool(bool1: bool = None):
    print("Yes" if bool1 else "No")


# d
def print_zugi(lst1: list[int]):
    for num in lst1:
        print(f"{num} is even" if num % 2 == 0 else f"{num} is odd")



# e
def my_statistics(grade_list: list[int]):
    print(f"Highest grade: {max(grade_list)}, lowest grade: {min(grade_list)}, amount of grades: {len(grade_list)}, average grades: {average(grade_list)}")





