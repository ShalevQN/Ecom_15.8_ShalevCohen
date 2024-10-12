'''
מחרוזות חלק ב' -
a. הסר את הרווחים משני הצדיים של המחרוזת הבאה : " day-fun "
b. בדוק אם המחרוזת "hello "מכילה אותיות בלבד. רמז isalpha
c. בדוק אם המחרוזת "777" מכילה מספרים בלבד. רמז isdigit
d. בדוק אם המחרוזת " " מכילה רווחים בלבד. רמז isspace
e. עבור הרשימה ['A ','J ','N ','I ','N['. צור ממנה מחרוזת אחת. רמז join
f. עבור אותה הרשימה- צור מחרוזת אחת עם '*' בין התווים. A*J*N*I*N. רמז join
g. תוך התעלמות מאותיות גדולות וקטנות: בדוק אם האות e מופיעה במילה hELLo
in, lower :רמז
h.* בונוס: קלוט מילה מהמשתמש, ואז באמצעות comprehension ייצר רשימה המכילה
כל אות כאיבר . כל אות תהיה גדולה. התעלם מספרות
['P',
'''

print("  fun-day  ".strip()) # a

print("hello".isalpha()) # b

print("777".isdigit()) # c

print("  ".isspace()) # d

e_str: str = "".join(['N', 'I', 'N', 'J', 'A']) # e
print(e_str)

f_str: str = "*".join(['N', 'I', 'N', 'J', 'A']) # f
print(f_str)

if "e" in "hELLo".lower(): print("e is in hELLO") # g

bonus_list: list[str] = [i.upper() for i in input("Enter a sentence: ") if i.isalpha()] # h - bonus
print(bonus_list)