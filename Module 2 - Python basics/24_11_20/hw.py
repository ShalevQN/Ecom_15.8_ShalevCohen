# 1

tup1: tuple[int] = (99,) # a

tup2: tuple[int, int, int] = (77, 88, 99) # b

def tup_length_return(t: tuple): # c
    return len(t)
#print(tup_length_return(tup2))

def two_tup_add(f_tuple: tuple, s_tuple: tuple): # d
    return f_tuple + s_tuple
#print(two_tup_add(tup1, tup2))

def two_tup_common(f_tuple: tuple, s_tuple: tuple): # e
    return tuple([x for x in f_tuple if x in s_tuple])
#print(two_tup_common(tup1, tup2))

def two_tup_uncommon(f_tuple: tuple, s_tuple: tuple): # f
    return tuple([x for x in f_tuple if not x in s_tuple] + [x for x in s_tuple if x not in f_tuple])
#print(two_tup_uncommon(tup1, tup2))

def finding_value_tup(x_tuple: tuple, index): # g
    try:
        return x_tuple[index]
    except IndexError:
        return None
#print(finding_value_tup(tup2, 3))

def reverse_tup(x_tuple): # h
    return tuple(list(x_tuple)[::-1])
#print(reverse_tup(tup2))

def mul_tup(x_tuple, y): # i
    return x_tuple * y
#print(mul_tup(tup2, 3))

def removing_from_tuple(x_tuple, y): # j
    return tuple([num for num in x_tuple if num != y])
#print(removing_from_tuple(tup2, 99))

def removing_dupes_tuple(x_tuple): # k
    temp_list: list = []
    for num in x_tuple:
        if num in temp_list:
            pass
        else:
            temp_list.append(num)
    return tuple(temp_list)
#tup3 = (99, 33, 22, 99, 22)
#print(removing_dupes_tuple(tup3))

def all_index_from_num_tup(x_tuple, y): # l - BONUS
    temp_list: list = list(x_tuple)
    r_list: list = []
    for i, num in enumerate(temp_list):
        if num == y:
            r_list.append(i)
    return tuple(r_list)
tup4: tuple = (10, 8, 5, 5, 3, 2, 5, 10, 30, 40)
#print(all_index_from_num_tup(tup4, 5))

# m
names_list: list[str] = []
grades_list: list[int] = []

while True:
    name_input = input("Enter a name: ")
    if name_input.lower() == "done":
        while True:
            grade_input = int(input("Enter a grade: "))
            if grade_input == -999:
                break
            else:
                grades_list.append(grade_input)
        break
    else:
        names_list.append(name_input)
name_grade_zipped = zip(names_list, grades_list)
#print(tuple(name_grade_zipped))

# 2
"""
The difference between a list and a tuple is that a list is mutable (can changes the items inside after creating it) and a tuple is not. list - [] tuple - ()
"""


# 3
"""
The code is not raising an error because line 4 and 5 does not change the tuple, but changes the dict in the tuple.
"""