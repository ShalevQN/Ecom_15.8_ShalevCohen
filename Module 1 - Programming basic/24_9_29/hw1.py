'''
רשימות comprehension
a. בשורה אחת - צור רשימה של מספרים מ 95-105
b. בשורה אחת - צור רשימה של מספרים זוגיים מ 10-20
כלומר: ,10 ,12 ,14 ,16 ,18 20
c. בשורה אחת - צור רשימה של 5 איברים אקראיים של False True
d. בשורה אחת - צור רשימה של 10 מספרים אקראיים בטווח 1-100
e. בשורה אחת - מהרשימה שיצרת בסעיף הקודם, צור רשימה המכילה רק את המספרים
הגדולים מ- 50
f.* בונוס: האם תוכל בשורה אחת לבצע את 2 הסעיפים הקודמים?
g.* בונוס: קלוט מחרוזות מהמשתמש. בשורה אחת צור רשימה המכילה את כל האותיות
שהקליד חוץ מהאות t וחוץ מ- רווח.
לדוגמא אם המשתמש הכניס masters python hello
]'h', 'e', 'l', 'l', 'o', 'p', 'y', 'h', 'o', 'n', 'm', 'a', 's', 'e', 'r', 's'[ :הרשימה תהיה התשובה
h. בשורה אחת - צור רשימה של 10 מספרים אקראיים בטווח 10-99
הדפס את הרשימה
כעת בשורה אחת - צור רשימה של 10 מספרים שיכילו רק את ספרת האחדות של
האיברים מהרשימה הקודמת. לדוגמא:
אם הרשימה הראשונה היתה – ,44 ,19 ,99 51 ...
הרשימה השנייה תהיה – ,4 ,9 ,9 1 ....
'''

import random

list_95to105: list[int] = [i for i in range(95, 105 + 1)] # a

list_10to20_even: list[int] = [i for i in range(10, 20 + 1, 2)] # b
list_10to20_even_2: list[int] = [i for i in range(10, 20 + 1) if i % 2 == 0]
print(list_10to20_even, list_10to20_even_2)

list_5_random_True_False: list[bool] = [random.choice([True, False]) for i in range(5)] # c
print(list_5_random_True_False)

list_10_random_1to100: list[int] = [random.choice(range(1, 100 + 1)) for _ in range(10)] # d
print(list_10_random_1to100)

list_10_random_1to100_above50: list[int] = [i for i in list_10_random_1to100 if i > 50] # e
print(list_10_random_1to100_above50)

bonus_question_1: list[int] = [i for i in [random.choice(range(1, 100 + 1)) for _ in range(10)] if i > 50] # f
print(bonus_question_1)

bonus_question_2: list[str] = [char for char in input("Enter a sentence: ") if not (char == "t" or char == " ")] # g
print(bonus_question_2)

list_random_10to99: list[int] = [random.choice(range(10, 100)) for _ in range(10)] # h
print(list_random_10to99)

list_random_10to99_ahadot = [i % 10 for i in list_random_10to99]
print(list_random_10to99_ahadot)

#list_random_10to99_ahadot = [i % 10 for i in [random.choice(range(10, 100)) for _ in range(10)]] ### both in one line......