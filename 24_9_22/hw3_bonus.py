lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
    user_input = int(input("Number to append: "))
    if user_input == -999:
        print("Ok. Done.")
        break
    else:
        inserted = False
        for i in range(len(lst)):
            if user_input < lst[i]:
                lst.insert(i, user_input)
                inserted = True
                break
        if not inserted:
            lst.append(user_input)
        print(lst)