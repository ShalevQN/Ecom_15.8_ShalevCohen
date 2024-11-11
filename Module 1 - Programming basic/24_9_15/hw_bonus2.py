'''
קלוט מספר שלם מהמשתמש (int) אם המספר מתחלק ב- 5 ללא שארית הדפס "Fizz",
אם המספר מתחלק ב- 3 ללא שארית הדפס "Buzz".
 אם המספר מתחלק גם ב- 3 ללא שארית וגם ב- 5 ללא שארית הדפס "Fizz Buzz" (רמז בדוק אם הסמפר 0== 5 %, בדוק אם המספר 0 == 3 %)
'''

user_input: int = int(input("Number: "))
if user_input % 5 == 0 and user_input % 3 == 0:
    print("Fizz Buzz")
elif user_input % 5 == 0:
    print("Fizz")
elif user_input % 3 == 0:
    print("Buzz")
else:
    print("Sorry. No output.")

### Another vers...
# user_input: int = int(input("Number: "))
# result: str = ""
# if user_input % 5 == 0:
#     result += "Fizz "
# if user_input % 3 == 0:
#     result += "Buzz "
# else:
#     if user_input % 5 != 0:
#         result += "Sorry, nothing."
# print(result)