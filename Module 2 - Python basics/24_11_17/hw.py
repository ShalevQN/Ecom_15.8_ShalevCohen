# 1

israel_dict: dict = {"name": "Israel", "birth": 1948, "population_millions": 9.3, "capital": "Jerusalem", "language": "Hebrew",
               "cities": ['Jerusalem', 'Tel Aviv', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'], "currency": "ILS", "area_Kilometer": 22145, "gpd_billion": 450}

print("Capital of Israel: ", israel_dict.get("capital")) # a

print(israel_dict.keys()) # b

print(israel_dict.values()) # c

for key, value in israel_dict.items(): # d
    print(f"{key}: {value}")

israel_dict_new = israel_dict.copy() # e

print(israel_dict_new.pop("gpd_billion")) # f

new_country_dict = dict.fromkeys(israel_dict.keys(), None) # g
print(new_country_dict)

for key in new_country_dict:
    new_country_dict[key] = input(f"Enter {key}: ")

print(new_country_dict)

# 2
print(len([w for w in input("Enter a sentence: ").split(" ")][-1])) # first try

# after chatgpt evaluation and consult (said I should avoid edge cases - didnt think of the possibility of a user putting space and the end of the string):
user_input = input("Enter a sentence: ").strip()
if not user_input:
    print(0)
else:
    print(len(user_input.split()[-1]))