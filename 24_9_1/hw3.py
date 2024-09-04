'''
כתוב תוכנית פייטון הקולטת 2 מחרוזות ומדפיסה אותם עם כוכבית ביניהם וגם עם מינוס ביניהם.
לדוגמא אם נקלטו המחרוזות הבאות : "rocks" "python"
יודפס:

*python*rocks*
-python-rocks-
'''

first_str: str = input("First string: ")
second_str: str = input("Second string: ")

print(f"*{first_str}*{second_str}*")
print(f"-{first_str}-{second_str}-")