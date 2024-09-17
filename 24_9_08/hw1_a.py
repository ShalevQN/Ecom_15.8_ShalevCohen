'''
אמא של דני הזמינה פיצה לכל החברים. היא מקפידה שכ ל חבר יקבל כמות
זהה של משולשי פיצה . כל אחד חייב לקבל מספר שלם של משולשי פיצה.
הגיעו לדני 4 חברים.
בואו נחשב כמה פיצות כל חבר קיבל וכמה נשארו )זכור: כל חבר
מקבל מספר זהה ושלם של משולשי פיצה(:
עבור 3 משולשים. כל חבר קיבל 0 ונשארו 3
עבור 4 משולשים. כל חבר קיבל משולש 1 ונשארו 0
עבור 6 משולשים. כל חבר קיבל משולש 1 ונשארו 2
עבור 8 משולשים. כל חבר קיבל 2 משולשים ונשארו 0
וכן הלאה ...
- כתוב תוכנית בפייטון הקולטת מספר של משולשי פיצה וכותבת כמה כל חבר קיבל וכמה
נשארו )עבור 4 חברים(
'''


people_num = 4
slices_num = int(input("There are 4 kids, every kid gets even amount of slices. How many slices? "))

slices_per_person = slices_num // people_num
remainder_slices = slices_num % people_num

if remainder_slices == 0:
    print(f"Each kid got {slices_per_person}.")
elif remainder_slices != 0:
    print(f"Each kid got {slices_per_person} and {remainder_slices} slices remained on the table.")
