'''
from the previous task...
כתוב תוכנית בפייטון הקולטת כמה חברים הגיעו לדני , לאחר מכן קולטת כמה משולשי פיצה
הוזמנו ואז מדפיסה כמה משולשי פיצה כל חבר קיבל וכמה נשארו
'''


people_num = int(input("How many kids invited to the party?"))
slices_num = int(input(f"Okay, {people_num} invited. \nEvery kid gets even amount of slices, how many slices should we order for them? "))

slices_per_person = slices_num // people_num
remainder_slices = slices_num % people_num

if remainder_slices == 0:
    print(f"Each kid got {slices_per_person}.")
elif remainder_slices != 0:
    print(f"Each kid got {slices_per_person} and {remainder_slices} slices remained on the table.")
