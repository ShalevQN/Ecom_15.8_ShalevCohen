'''
קלוט 2 מספרים שלמים והדפס אותם בסדר עולה )רמז: העזר בסעיף קודם(
אם לדוגמא נקלטו המספרים 10 ו - :1 יודפס-

1
10

אם לדוגמא נקלטו המספרים 6 ו - :19 יודפס-

6
19

אם המספרים זהים, יודפסו 2 המספרים )אין חשיבות לסדר(
'''

a: int = int(input("First Num: "))
b: int = int(input("Second Num: "))

if a<b:
    print(a)
    print(b)
elif a>b:
    print(b)
    print(a)
else:
    print(f"{a} and {b} not in an particular order.")