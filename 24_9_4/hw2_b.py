### Previous questions.

test_results: int = int(input("What's the grade u got?: "))

match test_results:
    case x if 0 < x < 40:
        print("try harder next time...")
    case x if 41 < x < 60:
        print("you're getting there, need some more work")
    case x if 61 < x < 80:
        print("pretty good")
    case x if 81 < x < 95:
        print("awesome!")
    case x if 96 < x < 100:
        print("excellent!!! You're a Star!")
    case _:
        print("illegal grade")