import random

# 1
# א
city_list: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

print("City length: ", sorted(city_list, key= lambda c: len(c))) # a

print("City number of words: ", sorted(city_list, key= lambda c: c.count(" "))) # b

print("City last letter: ", sorted(city_list, key= lambda c: c[-1])) # c

print("City name reversed: ", sorted(city_list, key= lambda c: c[0], reverse=True)) # d

print("City number of times 'a' showed up: ", sorted(city_list, key= lambda c: c.count("a"))) # e - BONUS

# f
city_list_miles: list[list[str|int]] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050, "Europe"], ["London", 2240, "Europe"],
                                        ["Sydney", 8780, "Australia"], ["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]

print("Distance from Israel: ", sorted(city_list_miles, key= lambda c: c[1])) #א

print("Distance from Israel from big to small: ", sorted(city_list_miles, key= lambda c: c[1], reverse=True)) #ב

print("By name of continent: ", sorted(city_list_miles, key= lambda c: c[2])) #ג

print("By continent name and distance from Israel: ", sorted(city_list_miles, key= lambda c: (c[2], c[1]))) #ד

# ב
random_numbers = [random.randint(1, 100) for _ in range(50)]

print("Random numbers going up: ", sorted(random_numbers)) # 1

#print("average: ", sum(random_numbers) // len(random_numbers))
print("Random numbers from their closeness to the average: ", sorted(random_numbers, key=lambda x: (x - (sum(random_numbers) // len(random_numbers))) ** 2)) # 2

# 2
text : str = ("This chocolate cake is rich, moist, and full of delicious chocolate flavor. To make the cake, you will need chocolate, flour, sugar, eggs, and butter. "
                  "After baking the chocolate cake, let the cake cool before adding the chocolate frosting.")

# cleaning text from punctuation and upper case
text = text.replace(",", "")
text = text.replace(".", "")
text = text.lower()
#print(text)

# a
text_w_dict: dict[str:int] = {}

for word in text.split(" "):
    if word in text_w_dict:
        text_w_dict[word] += 1
    else:
        text_w_dict[word] = 1
text_w_dict = dict(sorted(text_w_dict.items(), key=lambda c: c[1], reverse=True))
print("All of the words: ", text_w_dict)
print("Word repeated most times:", max(text_w_dict, key=text_w_dict.get), ", times: ", text_w_dict[max(text_w_dict, key=text_w_dict.get)])

# b
text_c_dict: dict[str:int] = {}
for char in text:
    if char == " ":
        continue
    if char in text_c_dict:
        text_c_dict[char] += 1
    else:
        text_c_dict[char] = 1
text_c_dict = dict(sorted(text_c_dict.items(), key=lambda c: c[1], reverse=True))
print("All of the letters: ", text_c_dict)
print("Letter repeated most times:", max(text_c_dict, key=text_c_dict.get), ", times: ", text_c_dict[max(text_c_dict, key=text_c_dict.get)])

# 3
num_dict: dict[str:int] = {} # made the key a str so the key and the value is easily differentiable

for x in range(1, 20 + 1):
    num_dict[f"{x}"] = x ** 3
#print("Num dict (value is the key by the power of 3): ", num_dict)

user_input: str = input("Enter a num (1-20) for it to power by 3: ")

try:
    print(num_dict[user_input])
except KeyError:
    print("not exist")
    #print(f"The input {user_input} is not in the dictionary.")