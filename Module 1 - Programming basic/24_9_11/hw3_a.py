'''
בתרגילים הבאים פתור באמצעות לולאת for, או לולאת while, או לולאת break-true-white:
'''

# קלוט מהמשתמש את גובהו )עשרוני( , עד אשר יתקבל גובה בין 0.4 לבין 2.5
# בכל פעם שיתקבל גובה שלא בטווח הזה, הדפס : input wrong

while True:
    height: float = float(input("How tall are you? "))
    if 0.4 <= height <= 2.5:
        print(f"Your height is {height} meters")
        break
    else:
        print("Wrong input...")