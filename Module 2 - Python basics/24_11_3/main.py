from func_without_return import *

# a
my_ascending(7, -12)

# b
my_details("AI is the best")

# c
say_bool(True)
say_bool(False)

# d
print_zugi([14, 14, 15, 10, 2, 3, 5])

# e
grade_list: list[int] = []
while True:
    try:
        user_input: int = int(input("Enter a grade: "))
        if user_input == -99:
            my_statistics(grade_list)
            break
        if 0 < user_input < 100:
            grade_list.append(user_input)
    except Exception as e:
        print("Your number could not be appended. reason:", e)


from func_with_return import *
# a
avg1 = my_avg(90, 99)
print(avg1)
# shortcut - print(my_avg(90, 99))

# b
head1 = my_headline("python has concurred the world")
print(head1, head1)

# c
res_con = concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9])
print(f"{res_con} length- {len(res_con)}")