'''
כתוב תוכנית פייטון הקולטת מהמשתמש את ה- id שלו כמחרוזת, את שמו הפרטי כמחרוזת, את
שם המשפחה שלו כמחרוזת, את הגובה שלו כעשרוני ) float), את שנת הלידה כמספר שלם )int )
כעת הדפס את הפרטים באמצעות ("..."f(print בפורמט הבא:

#id: 1 name: cohen , danny height: 1.87 year-of-birth: 2001
-- בדוגמא רואים את ההדפסה לאחר שנקלט id ,1 שם פרטי danny, שם משפחה cohen,
גובה 1.87 ושנת לידה 2001
-- היכן שמודגש זה הקלט שהגיע מהמשתמש )רמז: נשתמש ב - } {(, שאר הטקסט זה טקסט קבוע
-- קלוט פרטי 3 משתמשים והצג אותם זה מתחת לזה, שהכול יופיע מיושר כמו בטבלה,
רמז: השתמש ב ("..."f(print עם הסימן "<" וכו' )כפי שעשינו בשיעור(
'''

st_id = input("Whats your ID?: ")
st_first_name = input("What is your first name?: ")
st_last_name = input("What is your last name?: ")
st_height: float = float(input("What is your height?: "))
st_year_of_birth: int = int(input("What year were you born?: "))

nd_id = input("Whats your ID?: ")
nd_first_name = input("What is your first name?: ")
nd_last_name = input("What is your last name?: ")
nd_height: float = float(input("What is your height?: "))
nd_year_of_birth: int = int(input("What year were you born?: "))

rd_id = input("Whats your ID?: ")
rd_first_name = input("What is your first name?: ")
rd_last_name = input("What is your last name?: ")
rd_height: float = float(input("What is your height?: "))
rd_year_of_birth: int = int(input("What year were you born?: "))


print(f"#id: {st_id:<11} name: {st_last_name:<11} , {st_first_name:<11} height: {st_height:<11} year-of-birth: {st_year_of_birth:<11}")
print(f"#id: {nd_id:<11} name: {nd_last_name:<11} , {nd_first_name:<11} height: {nd_height:<11} year-of-birth: {nd_year_of_birth:<11}")
print(f"#id: {rd_id:<11} name: {rd_last_name:<11} , {rd_first_name:<11} height: {rd_height:<11} year-of-birth: {rd_year_of_birth:<11}")