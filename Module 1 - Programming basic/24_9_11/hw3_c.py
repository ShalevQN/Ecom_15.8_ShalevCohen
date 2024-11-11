# ערכו של פאי )pie )הוא .3.14 שאל את המשתמש כמה שווה פאי? וקלוט את תשובתו
# בלולאה עד אשר יקליד את התשובה הנכונה. יש למשתמש 3 נסיונות בלבד .
# אם הצליח בתוך 3 נסיונות )או פחות(, הדפס: "correct are you"
# אם נכשל 3 פעמים צא מהלולאה והדפס: " 3.14 is pie "

num = 3 # 3 tries

while True:
    user_input = float(input("What is the number of pie? "))
    if user_input == 3.14:
        print("You are correct!")
        break
    elif num == 1:
        print("No, pie is 3.14.")
        break
    else:
        print("No, try again.")
        num -= 1

