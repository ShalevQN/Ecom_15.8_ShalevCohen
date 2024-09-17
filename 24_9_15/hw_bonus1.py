'''
קלוט מספרים מהמשתמש , כל עוד המספר שנקלט מתחלק ב - 7 ללא שארית
ברגע שייקלט מספר שאיננו מתחלק ב - 7 ללא שארית )לדוגמא 10(, צא מהלולאה ואז
הדפס כמה מספרים המתחלקים ב- 7 ללא שארית נקלטו.
אם המשתמש הכניס מספר המתחלק ב- 11 ללא שארית )לדוגמא 33( , צא ב- break
מהלולאה, ואל תדפיס כמה מספרים נקלטו . רמז - else while
לדוגמא עבור : ,14 ,21 ,28 ,35 ,105 12 יודפס 6
לדוגמא עבור : ,63 ,7 ,42 77 לא יודפס כלום )מכיוון ש- 77 מתחלק ב- 11 ללא שארית(
'''

output_7 = 0
user_input = int(input("Number: "))
while user_input % 7 == 0 and user_input % 11 != 0:
    output_7 += 1
    user_input = int(input("Number: "))
else:
    if user_input % 11 != 0:
        print(output_7)


### other vers (with me not doing the while-else)
# while True:
#     user_input: int = int(input("Number: "))
#     if user_input % 7 == 0: # can add "and user_input % 11 != 0" here
#         output_7 += 1
#     if user_input % 11 == 0:
#         break
#     if user_input % 7 != 0:
#         print(output_7)
#         break