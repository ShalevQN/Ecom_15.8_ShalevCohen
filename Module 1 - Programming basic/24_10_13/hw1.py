'''
עבודת סוכות - הכנה למבחן

תנאים:
.1 קל ווט מספר עשרוני, אם הוא גדול מ 10- הדפס את ההפרש בינו לבין ,10 אחרת הדפס את מכפלתו
ב- .10
o דוגמה :אם נקלט המספר ,15 יודפס 5 )כי 15 - 10 = 5(.
אם נקלט המספר ,8 יודפס 80 )כי 8 * 10 = 80(.

.2 קל וט שלושה מספרים עשרוניים והדפס את הסכום שלהם רק אם הסכום גדול מ.100- אחרת הדפס
"הסכום קטן מ.100-"
o דוגמה :אם נקלטו המספרים ,30 40 ו ,50- יודפס 120 )כי הסכום גדול מ 100-(.
אם נקלטו המספרים ,10 20 ו,30- יודפס "הסכום קטן מ.100-"

.3 *בונוס/רשות : קלט שני עשרוניים והדפס את השבר הגדול יותר. אם השברים שווים הדפס "שווים."
o דוגמה :אם נקלטו המספרים 3.75 ו,9.5- יודפס .0.75 רמז השתמש ב int
אם נקלטו המספרים 2.5 ו,1.5- יודפס "שווים."

.4 קל וט גיל וודא שהוא תקין )מעל 0 ומתחת 120(. אם הוא לא תקין הדפס "גיל לא תקין."
o דוגמה :אם נקלט הגיל ,25 יודפס .25
אם נקלט הגיל ,130 יודפס "גיל לא תקין ."
.5 קל וט מספר תלת ספרתי והדפס את הספרה האמצעית שלו.
o דוגמה :אם נקלט המספר ,149 יודפס .4
אם נקלט המספר ,567 יודפס .6

לולאות:
.6 קל וט מספר טבעי n והדפס את כל המספרים השלמים מ n-עד 1 בסדר יורד.
o דוגמה :אם נקלט 5, = n יודפס: ,5 ,4 ,3 ,2 .1
.7 קל וט שני מספרים והדפס את כל המספרים הזוגיים בין הראשון לשני.
o דוגמה :אם נקלטו 4 ו,10- יודפסו: ,4 ,6 ,8 .10
אם נקלטו 7 ו,13- יודפסו: ,8 ,10 .12

.8 קל וט מספר חיובי n והדפס את כל המספרים עד n שהם מתחלקים ב3- או ב ,5- או בשניהם.
o דוגמה :אם נקלט 15, = n יודפס: ,3 ,5 ,6 ,9 ,10 ,12 .15
.9 קל וט מספר n והדפס את כל המספרים שהינם כפולות של 7 עד n
o דוגמה :אם נקלט 30, = n יודפסו: ,7 ,14 ,21 .28

עיבוד נתונים :
.11 קל וט מספרים עד שנקלט המספר ,0 הדפס את סכום המספרים השליליים שנקלטו.
• דוגמה :אם נקלטו המספרים: ,-3 ,91 -5 , ,-2 ,4 0 יודפס: -10 )כי -3 + -5 + -2 = -10( .
.12 קל וט רשימה של 10 מספרים והדפס את המספרים בסדר הפוך.
• דוגמה :אם נקלטו: ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 יודפסו: ,10 ,9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 .1
.13 קל וט סדרה של מספרים עד שנקלט המספר ,0 והדפס כמה מהמספרים שהוזנו הם ראשוניים.
• דוגמה :אם נקלטו המספרים: ,2 ,3 ,4 ,5 ,0 יודפסו: 3 )כי ,2 3 ו- 5 הם ראשוניים(.
.14 קל וט 5 מספרים והדפס את הממוצע שלהם, והדפס גם את כמות המספרים הגדולים מהממוצע.
• דוגמה :אם נקלטו המספרים: ,10 ,20 ,30 ,40 ,50 הממוצע הוא ,30 ויש 2 מספרים גדולים
מהממוצע.(50 40,)
.15 קל וט שני מספרים והדפס את תוצאת החילוק שלהם תוך שימוש בהפחתות בלבד.
• דוגמה :אם נקלטו המספרים 20 ו,5- התוצאה היא 4 )כי 20/5 = 4(.
אתגרים :
.16 קל וט מספר תלת ספרתי והדפס אם סכום הספרות שלו מתחלק ב .3-
• דוגמה :אם נקלט המספר ,123 הסכום הוא 1 + 2 + 3 = ,6 ולכן יודפס "מתחלק ב .3-"
אם נקלט המספר ,124 הסכום הוא ,7 ולכן יודפס "לא מתחלק ב .3-"
.17 קל וט מחרוזת ובדוק אם היא מהופכת )למשל: "אבבא" הפוך לאבבא(.
• דוגמה :אם נקלטה המחרוזת "אבבא", התשובה תהיה "מהופכת."
אם נקלטה המחרוזת "שלום", התשובה תהיה "לא מהופכת ."

בהצלחה

את שיעורי הבית יש להגיש ל - com.gmail@1train250824+pythonai
'''
from itertools import count

### Conditions

# 1
num: float = float(input("Enter a num: "))
print(f"{num - 10 if num > 10 else num * 10}")

# 2
sum_nums: float = float(input("Enter a num: ")) + float(input("Enter a num: ")) + float(input("Enter a num: "))
print(f"{"The sum is lower than 100." if sum_nums < 100 else sum_nums}")

# 3 - bonus
remainder_float1: float = (float(input("Enter a num: ")) * 10) % 10
remainder_float2: float = (float(input("Enter a num: ")) * 10) % 10

print(remainder_float1 / 10 if remainder_float1 > remainder_float2 else "Even" if remainder_float1 == remainder_float2 else remainder_float2 / 10)

# 4
age_input: int = int(input("Enter age: "))
print(age_input if 0 < age_input < 120 else "Invalid number")

# 5
print(input("Enter three digit number: ")[1])

### Loops
# 6
counter: int = int(input("Enter a nature number: "))
while counter > 0:
    print(counter, end=" ")
    counter = counter - 1

# 7
for x in range(int(input("Enter a num: ")), int(input("Enter a second num: ")) + 1):
    if x % 2 == 0:
        print(x, end=" ")

# Comprehended:
# print([x for x in range(int(input("Enter a num: ")), int(input("Enter a second num: ")) + 1) if x % 2 == 0])

# 8
for x in range(1 , int(input("Enter a num: ")) + 1):
    if x % 3 == 0 or x % 5 == 0:
        print(x, end=" ")

# Comprehended:
# print([x for x in range(1 , int(input("Enter a num: ")) + 1) if x % 3 == 0 or x % 5 == 0])

# 9
for x in range(1 , int(input("Enter a num: ")) + 1):
    if x % 7 == 0:
        print(x, end=" ")

# Comprehended:
# print([x for x in range(1 , int(input("Enter a num: ")) + 1) if x % 7 == 0])

### Data Processing
# 11
minuses_sum: int = 0
while True:
    x = int(input("Enter a number: "))
    if x < 0:
        minuses_sum = minuses_sum + x
    if x == 0:
        print(minuses_sum)
        break

# 12
number_reverse_list: list[int] = []
for _ in range(10):
    number_reverse_list.append(int(input("Enter a num: ")))
print(number_reverse_list[::-1])

# 13
prime_numbers_list: list[int] = []
while True:
    prime_check = int(input("Enter a num: "))
    if prime_check > 1:
        for i in range(2, prime_check):
            if (prime_check % i) == 0:
                #print("not a prime number")
                break
        else:
            prime_numbers_list.append(prime_check)
    if prime_check == 0:
        print("Prime numbers:", " ".join(str(x) for x in prime_numbers_list))
        break

# 14
nums: list[int] = []
for _ in range(5):
    nums.append(int(input("Enter a num: ")))
avg_nums = sum(nums) / len(nums)
print(f"avg: {avg_nums}")
print([num for num in nums if num > avg_nums])

# 15
input_num1: int = int(input("Enter num 1: "))
input_num2: int = int(input("Enter num 2: "))
counter: int = 0
while input_num1 > 0:
    counter = counter - 1 # had to use subtraction...
    input_num1 = input_num1 - input_num2
print(f"Answer is {-counter}") # converting it back to positive number :)

### Challenges ###
# 16
num: int = int(input("Enter a three digit number: "))
sum_digits: int = 0
while num > 0:
    sum_digits = sum_digits + (num % 10)
    num = num // 10
print(f"{sum_digits}is divisible by 3" if sum_digits % 3 ==0 else f"{sum_digits} is not divisible by 3")

# 17
str_17 = input("Enter a word: ")
print(f"{str_17} is reversible" if str_17[::-1] == str_17 else f"{str_17} is not reversible")