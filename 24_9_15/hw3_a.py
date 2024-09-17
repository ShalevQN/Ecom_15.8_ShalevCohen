'''
see hw3
'''

while True:
    user_input: int = (int(input("What is your number(0<)? ")))
    if user_input > 0:
        for x in range(1, user_input + 1):
            for y in range(x):
                z = y + 1
                print(z, end="")
            print("")
        for x in range(user_input -1, 0 , -1):
            for y in range(x):
                z = y + 1
                print(z, end="")
            print("")
        break
    else:
        print("I asked for a number greater than 0!")

