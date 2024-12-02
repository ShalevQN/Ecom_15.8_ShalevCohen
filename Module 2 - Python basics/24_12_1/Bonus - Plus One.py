def plus_one(arr: list[int]) -> list[int]:
    # string_digits: str = ""
    # for num in arr:
    #     string_digits += str(num)
    string_digits = str(int("".join(map(str, arr))) + 1)
    return [int(num) for num in string_digits]

print(plus_one([1,2,3]))
#print(plus_one([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))