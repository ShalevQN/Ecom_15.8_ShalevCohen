'''
השתמש בלולאת for והדפס:
- את כל המספרים השלמים מ- 0 ועד 10 כ ולל
- את כל המספרים הזוגיים מ 40- ועד 88 כולל
- את כל המספרים המתחלקים ב7- ) ללא שארית( מ77- ועד 105 כולל
- את כל המספרים המתחלקים ב- 3 )ללא שארית( מ 99- ועד 66 )בסדר יורד(
'''

for x in range(0,10 + 1):
    print(x, end=" ")

print("\n----------")
for x in range(-40, 88 +1, 2):
    print(x, end=" ")

print("\n----------")
for x in range(-77, 105 + 1):
    if x % 7 == 0:
        print(x, end=" ")
    else:
        pass

print("\n----------")
for x in range(99, 66 -1, -1):
    if x % 3 == 0:
        print(x, end=" ")
    else:
        pass