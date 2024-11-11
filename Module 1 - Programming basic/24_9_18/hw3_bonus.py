'''
*בונוס/רשות: קלוט מהמשתמש מספר אי-זוגי והדפס את הצורה הבאה.
לדוגמא , עבור המספר 5 הדפס את המעויין הבא:
   1
  123
 12345
  123
   1
'''


while True:
    user_input: int = (int(input("What is your number (odd and greater than 0)? ")))
    if user_input > 0 and user_input % 2 != 0:
        for x in range(0, user_input + 1):
            if x % 2 != 0:
                print(" " * ((user_input // 2) - (x // 2)), end="")
                for y in range(x):
                    print(y + 1, end="")
                print("")
        for x in range(user_input -1, 0 , -1):
            if x % 2 != 0 or x == 1:
                print(" " * ((user_input // 2) - (x // 2)), end="")
                for y in range(x):
                    print(y + 1, end="")
                print("")
        break
    else:
        print('I asked for an odd number and greater than 0!')