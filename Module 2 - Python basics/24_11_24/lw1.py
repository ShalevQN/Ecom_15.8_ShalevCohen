from datetime import datetime, timezone, timedelta
datetime.now().strftime("%H:%M:%S.%f %d/%m/%y")
new_list: list = []

user_input: str = input("Enter a name: ")

while not user_input == "done":
    new_list.append((user_input, datetime.now().strftime("%H:%M")))
    user_input: str = input("Enter a name: ")

for index, (key, value) in zip(range(len(new_list)), new_list):
    print(f"{index}: {key} {value}")
