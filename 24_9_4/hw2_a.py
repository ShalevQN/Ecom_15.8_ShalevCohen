'''
קלוט מהמשתמש ציון מבחן ) int )והדפס פידבק באופן הבא:
match case ב if-elif-else ב השתמש
"try harder next time..." הדפס :0-40 בין ציון עבור .a
"you're getting there, need some more work" הדפס :41-60 בין ציון עבור .b
c. עבור ציון בין :61-80 הדפס "good pretty"
d. עבור ציון בין :81-95 הדפס "!awesome"
"excellent!!! You're a Star!" הדפס :96-100 בין ציון עבור .e
f. עבור ציון קטן מ - 0 או גדול מ - :100 הדפס "grade illegal"
'''


test_results: int = int(input("What's the grade u got?: "))

if 0 <= test_results <= 40:
    print("try harder next time...")
elif 41 <= test_results <= 60:
    print("you're getting there, need some more work")
elif 61 <= test_results <= 80:
    print("pretty good")
elif 81 <= test_results <= 95:
    print("awesome!")
elif 96 <= test_results <= 100:
    print("excellent!!! You're a Star!")
else:
    print("illegal grade")

### Other option:
#elif 100 <= test_results or test_results <= 0:
#    print("illegal grade")