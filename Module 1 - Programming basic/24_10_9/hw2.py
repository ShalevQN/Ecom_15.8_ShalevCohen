'''
מחרוזות בסיס -
ייצר מחרוזת )אחת( של השם המלא שלך ועיר המגורים שלך. הקפד על רווח בין השמות
a. הדפס את אורך המחרוזת. רמז len
b. הדפס את המחרוזת כולה באותיות גדולות. רמז upper
c. הדפס את המחרוזת כולה באותיות קטנות. רמז lower
d. בדוק אם המחרוזת מתחילה בשם הפרטי שלך. רמז startswith
e. בדוק אם המחרוזת מסתיימת בעיר המגורים שלך. רמז endswith
f. פרק את המחרוזת לרשימה המכילה את שמך הפרטי, משפחה, עיר מגורים. רמז split
g. הפוך את הרווחים לכוכביות. רמז replace. לאחר מכן - פרק שוב את המחרוזת החדשה
לרשימה )כמו בסעיף הקודם (
h. הדפס את המחרוזת במרכז של 50 תווים, עטופה בתו "=". רמז center
i. הדפס את המחרוזת מהתו ה- 4 ועד הסוף
j. הדפס את המחרוזת מתחילתה ועד לתו ה- 4 )כולל(
k. הדפס את כל התווים הזוגיים במחרוזת
l. דאג שכל מילה במחרוזת תתחיל באות גדולה. רמז title
'''

info_str: str = "shalev cohen haifa"
print(info_str)
print("Length: ", len(info_str)) # a

print("Upper: ", info_str.upper()) # b

print("Lower: ", info_str.lower()) # c

if info_str.startswith("Shalev"): print("The string starts with first name.") # d

if info_str.endswith("Haifa"): print("The string ends with a city") # e

print(info_str.split(" ")) # f

new_info_str = info_str.replace(" ", "*") # g
print(new_info_str)
print(new_info_str.split("*"))


print(info_str.center(50, "=")) # h

print(info_str[3:]) # i

print(info_str[:4]) # j

print(info_str[1::2]) # k

print(info_str.title()) # l