'''
see "hw2"
'''


import random

print("Welcome\nIn this game you should guess one number between 1-100, the computer will tell you if the number you entered is bigger or smaller than the correct number.")

Random_Num: int = random.randint(1, 100)
guess_counter: int = 0

#print(Random_Num)

while True:
    user_input: int = int(input("Your Guess Number(1-100): "))
    guess_counter += 1
    if user_input > Random_Num:
        print("Your guessed number is too high")
    elif user_input < Random_Num:
        print("Your guessed number is too low")
    else:
        print("Your guessed number is exactly right!")
        print(f"Bingo! your number of guesses were: {guess_counter}")
        break

