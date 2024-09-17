age: int = int(input("Enter age: "))

match age:
    case 10 | 11 | 12:
        print("young")
    case 13 | 14 | 15:
        print("teenager")
    case 16| 17:
        print("young adult")
    case 18 | 19 | 20:
        print("adult")
    case _:
        print("old asf")