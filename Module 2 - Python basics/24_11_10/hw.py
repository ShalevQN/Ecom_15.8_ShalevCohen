import random

# 1 - using filter for int list
random_50_int: list[int] = [random.choice(range(1, 100 + 1)) for _ in range(50)]
#random_50_int.sort()
print("50 ints list: ", random_50_int)
print("nums bigger than 50: ", list(filter(lambda x: x > 50 , random_50_int))) # a
print("divisible by 7: ", list(filter(lambda x: x % 7 == 0 , random_50_int))) # b
print("two digit numbers: ", list(filter(lambda x: x in range(10, 100) , random_50_int))) # c
print("two digit numbers that are the same digit: ", list(filter(lambda x: x in range(10, 100) and (x // 10) == (x % 10) , random_50_int))) # d
print("numbers that sum of their digits are 9: ", list(filter(lambda x: (x // 10) + (x % 10) == 9 , random_50_int))) # e
random_ints_average = sum(random_50_int) // 50
#print("average: ", random_ints_average)
print("numbers that are above average: ", list(filter(lambda x: x > random_ints_average , random_50_int))) # f
print("numbers that are bigger than the half of the biggest number: ", list(filter(lambda x: x > max(random_50_int) // 2 , random_50_int))) # g


# 2 - using filter for string list
games_list: list[str] = ["Grand Theft Auto V","Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print("games that their name is bigger than 8 chars: ", list(filter(lambda x: len(x) > 8 , games_list))) # a
print("games that their name starts with f: ", list(filter(lambda x: x.startswith("F") , games_list))) # b
print("games that their name has 2 words exactly: ", list(filter(lambda x: x.count(" ") == 1 , games_list))) # c
print("games that has V in their name: ", list(filter(lambda x: "v" in x.lower() , games_list))) # d


# 3 - using map in num list
random_20_int: list[int] = [random.choice(range(-50, 50 + 1)) for _ in range(20)]
#random_20_int.sort()
print("20 ints list: ", random_20_int)
print("Every number in power of 3: ", list(map(lambda x: x ** 3, random_20_int))) # a
print("Only the first digit: ", list(map(lambda x: x if x / 10 < 1 and x > 0  else x % 10 if x > 1 else -x if -x / 10 < 1 and -x > 0  else -x % 10, random_20_int))) # b
print("C to F: ", list(map(lambda x: round(x * 1.8 + 32, 2) , random_20_int))) # c
print("Positive to positive and negative to negative: ", list(map(lambda x: "Positive" if x > 0 else "Negative" , random_20_int))) # d - BONUS


# 4 - using map in string list
fruit_strs: list[str] = ["Mango", "Orange" ,"Banana" ,"Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print("Reversed: ", list(map(lambda x: x[::-1] , fruit_strs))) # a
print("First letter: ", list(map(lambda x: x[0] , fruit_strs))) # b
print("All upper case: ", list(map(lambda x: x.upper() , fruit_strs))) # c
print("Middle char: ", list(map(lambda x: x[len(x)//2] , fruit_strs))) # d
print("Reversed: ", list(map(lambda x: f"{x}!" if x.endswith("s") else x , fruit_strs))) # e - BONUS


# 5 - Global questions:
# A global in function allows to access a variable outside its current scope.
# The drawback of using global variables is that it is difficult to know which and how the variable changes.
# The error is caused because Python does not know where the x is defined, which can be fixed by using global statement in the function to "call" the variable and access it.