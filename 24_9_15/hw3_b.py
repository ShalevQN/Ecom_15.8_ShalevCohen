'''
see hw3
'''
# by the way, this was the hardest one for me until now!
while True:
    user_input = int(input("What is your number (odd number and 0<)? "))
    if user_input > 0 and user_input % 2 != 0:
        for i in range(0, user_input // 2 + 1):
            print(" " * (user_input // 2 - i), end="")
            print("*" * (2 * i + 1))
        break
    else:
        print("I asked for an odd number greater than 0!")


### Little bonus, added the user input as the number of iterations.
# while True:
#     user_input: int = (int(input("What is your number(0<)? ")))
#     if user_input > 0:
#         for x in range(1, user_input):
#             print(" " * (user_input - i - 1), end="")
#             print("*" * (2 * i + 1))
#         break
#     else:
#         print("I asked for a number greater than 0!")