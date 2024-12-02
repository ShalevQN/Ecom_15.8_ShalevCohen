array= [True, True, True, False, True, True]
def successive_check(bool_list: list[bool]):
    for i , object_bool in (1, enumerate(bool_list)):
        #print(i)
        # if i - 1 == -1:
        #     continue
        if object_bool == bool_list[i-1]:
            return i
    else: return -1
print("Successive Check: ", successive_check(array))