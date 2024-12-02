#1
# I used stack to answer this, following an explanation for me to understand this subject.
# * I answered this question from leet code a couple of days ago.
from collections import deque

def valid_parentheses(para_str: str) -> bool:
    """
    :param para_str: str:
    :return: Bool, True if all brackets are closed and in correct order and type. Returns False otherwise.
    """
    return_stack = deque() # stack
    bracket_dict: dict = {"(": ")", "[": "]", "{": "}"} # dict to compare brackets to their matching
    for bracket in para_str:
        if bracket in bracket_dict: # if bracket is opening bracket (bracket_dict.keys())
            return_stack.append(bracket)
        else:
            if not return_stack: # if queue is empty, return False - no brackets to compare
                return False
            if bracket_dict[return_stack.pop()] != bracket: # compare the bracket to their matching bracket. if not, return False
                return False
    return len(return_stack) == 0 # return True or False if there are any more brackets to close

print(valid_parentheses("[]"))

print(valid_parentheses("([{}])"))

print(valid_parentheses("[(])"))

#2
def removing_duplicates_list(lst_x: list[int]):
    """
    removing duplicates without using set, tuple or dict or count()
    :param lst_x: list[int]:
    :return:a new list containing unique items, in this case int
    """
    return_list = []
    for num in lst_x:
        if not num in return_list:
            return_list.append(num)
    return return_list

print(removing_duplicates_list([1,1,2,3,4,4]))

#3
def two_list_sort(lst_x: list[int], lst_y: list[int]):
    """
    sorting two lists without using sort() sorted() count() or set
    :param lst_x: list[int]:
    :param lst_y: list[int]:
    :return: new list sorted
    """
    return_list = lst_x.copy()
    for num in lst_y:
        for i in range(len(return_list)):
            if return_list[i] > num:
                return_list.insert(i, num)
                break
        else: # Not sure if we learned this, but just for clarification that I know what it does - for else executes when and only if the loop is finished and not broken.
            return_list.append(num)
    return return_list

print(two_list_sort([1,2,4], [1,3,4, 5 ,6]))