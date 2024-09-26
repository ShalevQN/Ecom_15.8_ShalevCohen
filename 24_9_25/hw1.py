# d:
# .extend() modifies the original list by adding the elements of another list.
# The + operator creates a new list without changing the original list.


temps: list[float] = [] # a

while True:
    user_input: float = float(input("Number: "))
    if user_input == -999: # b
        temps.extend([18.5 ,39.1 , -20.0]) # c
        #print(f"temps: {temps}")
        print(f"max: {max(temps)}") # e
        print(f"min: {min(temps)}")
        if 18.5 in temps: # f
            print(True)
        else:
            print(False)
        print(temps.count(-20.0)) # g
        print(f"avg: {sum(temps) / len(temps)}") # h
        for temp in temps: # i
            print(temp)
        if 39.1 in temps: # j
            print(temps.index(39.1))
        del temps[0] # k
        #print(temps)
        del temps[::2] # l
        #print(temps)
        if 18.5 in temps: # m      # What if theres no 18.5? (What if the last del removed 18.5?) - it would result in error
            temps.remove(18.5)
        temp_last = temps.pop() # n
        #print(temp_last)
        temps2 = temps.copy() # o
        temps2.sort()
        #print(temps2)
        temps3 = temps2.copy() # p
        temps3.sort(reverse= True)
        #print(temps3)
        break
    else:
        if -50 < user_input < 50:
            #print("appended.")
            temps.append(user_input)