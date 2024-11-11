lst1: list[int] = []

while True:
    user_input: int = int(input("Number between 0-10: "))
    if user_input == -999:
        break
    else:
        if user_input in range(10 + 1):
            lst1.append(user_input)
            #print(lst1)
            statistics_str = "Statistics: "
            for num in range(10 + 1):
                if lst1.count(num) > 0:
                    statistics_str = statistics_str + f"[{num}]: {lst1.count(num)} "
            print(statistics_str) # This could be pushed back 2 indents to print every "input" but I thought since it should really ignore numbers not from 0-10 then don't print...