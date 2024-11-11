'''
רשימות תנאים בולייאנים-
a. ייצר רשימה בת 3 איברים ושים בתוכה ערכים אקראיים
random choice - ב השתמש True False של
b. בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק True
c. בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות True אחד
d. בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק False
e. בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות False אחד
f. ייצר רשימה אקראית של חמישה מספרים בין 2 למינוס 2 )כלומר ,2 ,1 ,0 -1 , -2(
השתמש בפונקציות random
g. בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק מספרים שונים מ- 0
h. בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות איבר אחד שהוא לא 0
i. בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק- 0
j. בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות איבר אחד שהוא 0
'''

import random

three_bool: list[bool] = [random.choice([True, False]) for _ in range(3)] # a
print(three_bool)

print("only true: ",all(three_bool)) # b

print("at least one true: ",any(three_bool)) # c

print("only false: ", not all(three_bool)) # d

print("at least one false: ", not any(three_bool)) # e


five_random_numbers_between_minus2and2: list[int] = [random.choice(range(-2, 3)) for num in range(5)] # f
print(five_random_numbers_between_minus2and2)


print("all of them are not zero: ", all(five_random_numbers_between_minus2and2)) # g

print("at least one that is not zero: ", any(five_random_numbers_between_minus2and2)) # h

print("all zero: ", not any(five_random_numbers_between_minus2and2)) # i

print("at least one zero: ", not all(five_random_numbers_between_minus2and2)) # j