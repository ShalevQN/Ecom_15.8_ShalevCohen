'''
טיפול בשגיאות -
a. הסבר מה עו שה except-try?
b. הסבר מדוע כדאי "לתפוס" את השג יאות בפייטון?
c. כתוב קטע קוד המחלק את ה מספר 88 ב- אפס, ואז עטוף אותו ב - except try
d. כתוב קטע קוד המבצע raise לשגיאה, ואז עטוף אותו ב- except try
e. צור רשימה של מספרים באורך 4 והכנס לתוכה מספרים כלשהם
כתוב לולאה הקולטת מהמשתמש מספר עד אשר המשתמש הכניס מינוס 999
i. בכל פעם הדפס את איבר הרשימה באינ ד קס שהוכנס
)לדוגמא אם המשתמש הכניס ,0 הדפס את האיבר באינד קס 0(
ii. עטוף את הקוד ב except-try כך שאם המשתמש יכניס אות, או אינדקס שלא
בטווח - אז התוכנית לא תכשל

הוסף ל- except הדפסה המסבירה מה היתה הטעות )ראה קוד מהשיעור(
'''

# a- try-except is used for handling errors and allowing the program to continue running even if it encounters an error.
# b- catching errors prevents crashes, handles issues without stopping, and helps debugging.


try: # c
    x= 88 / 0
    print(x)

except ZeroDivisionError:
    print("88 cannot be divided by zero!")

# try: # d?
#     raise AttributeError
# except AttributeError:
#     print("a")

try: # d
    x = 5
    if x > 0:
        raise AttributeError

except AttributeError:
    print("Number is larger than 0")

list1 = [32, 48 , 76, 80] # e
print(list1)
while True:
    try:
        user_input: int = int(input("Enter a number (index): "))
        if user_input == -999:
            break
        print(list1[user_input])
    except Exception as e:
        print(f"The error is: {e}")