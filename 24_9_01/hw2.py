'''
כתוב תוכנית פייטון הקולטת 2 מספרים עשרוניים ) float :y float :x), מחשבת את ההפרש ביניהם
לתוך תא זיכרון נוסף ) float :diff ). לאחר מכן הדפס את ההפרש (diff(print
'''

x: float = float(input("First num: "))
y: float = float(input("Second num: "))

diff: float = x - y

print(diff)