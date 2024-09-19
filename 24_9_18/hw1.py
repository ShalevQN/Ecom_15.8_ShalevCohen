'''
ק לוט 10 מספרים מהמשתמש באמצעות לולאה.
אם הוכנס מספר גדול מ1000- או קטן ממינוס ,1000 התעלם מהמספר . רמז: continue
אם הוכנס מינוס ,9999 צא מהלולאה ואל תדפיס את הסטטיסטיקות
במידה ולא נקלט מינוס 999 הדפס את הסטטיסטיקות הבאות:
- כמה מספרים חיוביים נקלטו?
- כמה מספרים שליליים נקלטו ?
- כמה פעמים הוכנס המספר 0?
- כמה מספרים המתחלקים ב- 7 ללא שארית נקלטו?
- מה היה המספר החיובי האחרון שהוכנס? אם לא היה כזה, הדפס None
- מה היה המספר השלילי האחרון שהוכנס? אם לא היה כזה, הדפס None
)כדאי להשתמש בלולאה עם else- כדי לטפל במקרה שבו המספרים הוזנו בהצלחה ולא יצאת
מוקדם עם break בעקבות קלט של מינוס 999(
'''

positive_nums_count: int = 0
negative_nums_count: int = 0
num_zero_count: int = 0
divided_by_7_count: int = 0
last_positive_num = None
last_negative_num = None
loop_broke = False

for x in range(10):
    user_input: int = int(input("Enter a number: "))
    if user_input == -9999:
        loop_broke = True
        break
    elif -1000 <= user_input <= 1000:
        if user_input > 0:
            positive_nums_count += 1
            last_positive_num = user_input
        elif user_input < 0:
            negative_nums_count += 1
            last_negative_num = user_input
        if user_input == 0:
            num_zero_count += 1
        if user_input % 7 == 0:
            divided_by_7_count += 1
    else:
        continue

if not loop_broke:
    print(f"Statistics:\nPositive numbers entered: {positive_nums_count}\nNegative numbers entered: {negative_nums_count}\nTimes zero entered: {num_zero_count}"
          f"\nTimes the number could be divided by seven: {divided_by_7_count}\nLast positive number entered: {last_positive_num}"
          f"\nLast negative number entered: {last_negative_num}")
