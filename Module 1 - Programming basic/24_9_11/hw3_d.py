# קלוט מהמשתמש 3 מספרים בלולאה עד אשר :
# המספר הראשון שנקלט יהיה בין ,0-10
# + וגם המספר השני שנקלט יהיה בין ,10-60
# + וגם המספר השלישי שנקלט יהיה בין .60-100
# + וגם המספר השני שנקלט יהיה ממוצע של שלושת המספרים.
# לדוגמא : 10 50 90
# קלוט בלולאה את 3 המספרים שוב ושוב ... עד אשר כל התנאים יתק יימו

while True:
    first_num: int = int(input("First number: "))
    second_num: int = int(input("Second number: "))
    third_num: int = int(input("Third number: "))
    average_nums: int = (first_num + third_num) // 2
    print(average_nums)
    if 0 <= first_num <= 10 <= second_num <= 60 <= third_num <= 100 and second_num == average_nums:
        print(f"Nice! the second number ({second_num}) is equal to the average number ({average_nums})!")
        break