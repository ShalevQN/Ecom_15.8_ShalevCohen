'''
למערכת שמע יש להציג תיאור של רמת-ווליום
קלוט מהמשתמש רמת -ווליום )int )והדפס פידבק באופן הבא: )רמז- השתמש ב case match )
a. עבור 0 הדפס "mute "
"very quiet" הדפס 1 עבור .b
"very quiet" הדפס 2 עבור .c
d. עבור 3 הדפס " quiet "
"moderately quiet" הדפס 4 עבור .e
f. עבור 5 הדפס "medium "
"moderately loud" הדפס 6 עבור .g
h. עבור 7 הדפס "loud "
"very loud" הדפס 8 עבור .i
"extremely loud" הדפס 9 עבור .j
"extremely loud" הדפס 10 עבור .k
'''

volume: int = int(input("What is the volume? (0-10): "))
match volume:
    case 0:
        print("mute")
    case volume if 1 <= volume <= 2:
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9 | 10:
        print("extremely loud")
    case _:
        print("Choose a number between 0-10, any other numbers are disqualified.")


# def how_loud():
#     volume: int = int(input("What is the volume? (0-10): "))
#     match volume:
#         case 0:
#             print("mute")
#         case 1 | 2:
#             print("very quiet")
#         case 3:
#             print("quiet")
#         case 4:
#             print("moderately quiet")
#         case 5:
#             print("medium")
#         case 6:
#             print("moderately loud")
#         case 7:
#             print("loud")
#         case 8:
#             print("very loud")
#         case 9 | 10:
#             print("extremely loud")
#         case _:
#             print("Choose a number between 0-10, any other numbers are disqualified.")
#             how_loud()
#
# how_loud()