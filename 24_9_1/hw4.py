'''
קלוט 2 מספרים שלמים ) int :b int :a )והדפס את הגדול מבין שניהם
בדוק בתנאי אם b > a אם כן: הדפס את a אחרת: הדפס את b
'''

a: int = int(input("First Num: "))
b: int = int(input("Second Num: "))

if a<b:
    print(b)
else:
    print(a)
