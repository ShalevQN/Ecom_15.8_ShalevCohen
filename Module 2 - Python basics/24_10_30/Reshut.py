# a
school_student_count: int = 103
classroom_student_size: int = 30

print("Full classrooms: ", school_student_count//classroom_student_size)
print("Last classroom would have: ", school_student_count % classroom_student_size)

school_student_count: int = int(input("How many students: "))
print("Full classrooms:", school_student_count//classroom_student_size)
print("Last classroom would have: ", school_student_count % classroom_student_size)


# b
while True:
    b_user_input = None
    try:
        b_user_input = int(input("Enter a num: "))
        break
    except:
        continue
if 10 < b_user_input < 99:
    if int(str(b_user_input)[0]) > int(str(b_user_input)[1]):
        print(b_user_input)
    else:
        print(str(b_user_input)[::-1])

# c
for num in range(2,200 + 1):
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
    if prime:
       print(num, end=", ")

# d
a_count: int = 0
b_count: int = 0
c_count: int = 0
d_count: int = 0

while True:
    d_user_input: str = input("Enter a letter(a-d) or x to exit: ")
    match d_user_input:
        case "a":
            a_count = a_count+ 1
        case "b":
            b_count = b_count+ 1
        case "c":
            c_count = c_count+ 1
        case "d":
            d_count = d_count+ 1
        case "x":
            max_number_list: list = [a_count, b_count, c_count, d_count]
            letters = ["A", "B", "C", "D"]
            print(f"A: {a_count}, B: {b_count}, C: {c_count}, D: {d_count}.\nMost repeated answer: {letters[max_number_list.index(max(max_number_list))]}\nLeast repeated answer: {letters[max_number_list.index(min(max_number_list))]}")
            break
        case _:
            continue
