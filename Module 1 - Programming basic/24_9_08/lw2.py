'''input age
if the age is bigger equal 18 then is_old_enough = True otherwise be False
if old enough offer Beer else offer juice'''

age: int = int(input("What is your age? "))

if age > 18:
    print("offer beer")
else:
    print("offer juice")