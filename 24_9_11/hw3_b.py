#קלוט מהמתשתמש 2 מספרים )שלמים (. והדפס את המספרים השלמים ביניהם.
# לדוגמא אם נקלט 1 ו- 5 ה דפס: 1 2 3 4 .5 שים לב: המספר הראשון שנקלט לא בהכרח
# קטן מהמספר השני שנקלט. כלומר אם נקלט 5 ו- ,1 אז יודפס: 5 4 3 2 1

first_num: int = int(input("First number: "))
second_num: int = int(input("Second number: "))

if first_num > second_num:
    for x in range(first_num, second_num -1, -1):
        print(x, end=" ")
elif first_num < second_num:
    for x in range(first_num, second_num + 1):
        print(x, end=" ")
else:
    print("Same number? really?")