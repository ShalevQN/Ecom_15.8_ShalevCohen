statistics_list: list[int] = []
for x in range(100 + 1):
    statistics_list.append(0)

while True:
    user_input: int = int(input("Number between 0-100: "))
    if user_input == -999:
        print(statistics_list)
        break
    else:
        if user_input in range(100 + 1):
            statistics_list[user_input] = statistics_list[user_input] + 1
            statistics_str = "Statistics: "
            for i in range(100 + 1):
                if statistics_list[i] > 0:
                    statistics_str = statistics_str + f"[{i}]: {statistics_list[i]} "
            print(statistics_str)