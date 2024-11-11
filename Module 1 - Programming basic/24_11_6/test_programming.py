# Conditions

# 1 V
x_1: float = float(input("Enter first float: "))
y_1: float = float(input("Enter second float: "))
if x_1 < y_1:
    print(x_1)
    print(x_1)
    print(x_1)
else:
    print(y_1)
    print(y_1)
    print(y_1)

# 2 V
x_2: int = int(input("Enter first int: "))
y_2: int = int(input("Enter second int: "))

print("average:", (x_2 + y_2) / 2)

# 3 V
x_3: int = int(input("Enter first int: "))
y_3: int = int(input("Enter second int: "))
z_3: int = int(input("Enter third int: "))

print("average:", (x_3 + y_3 + z_3) / 3)

# 4 V
movie_minutes_long: int = int(input("Enter the length of the movie in minutes: "))
print("The movie is", (movie_minutes_long // 60), "hour(s)", "and", (movie_minutes_long % 60), "minute(s)")

# 5 V
num_5 = int(input("Enter a 4 digit number: "))
print(num_5 % 10)

# 6 V
num_6 = int(input("Enter a 4 digit number: "))
print((num_6 // 10) % 10)

# 7 V
twodigit_7: int = int(input("Enter a 2 digit number: "))
print("Sum of two digits:", (twodigit_7 % 10) + (twodigit_7 // 10))

# 8 V
twodigit_8: int = int(input("Enter a 2 digit number: "))
print(f"Reversed: {twodigit_8 % 10}{twodigit_8 // 10}")

# 9 V
print("even" if int(input("Enter a number: ")) % 2 == 0 else "odd")
int_9: int = int(input("Enter a number: "))
if int_9 % 2 == 0:
    print(f"{int_9} is an even number")
else:
    print(f"{int_9} is an odd number")

# 10 V
income_int: int = int(input("enter your salary (per month): "))
taxes = 0

if income_int <= 6000:
    taxes = 0
elif income_int <= 12000:
    taxes = (income_int - 6000) * 0.10
elif income_int <= 18000:
    taxes = (12000 - 6000) * 0.10 + (income_int - 12000) * 0.20
elif income_int <= 25000:
    taxes = (12000 - 6000) * 0.10 + (18000 - 12000) * 0.20 + (income_int - 18000) * 0.30
elif income_int <= 35000:
    taxes = (12000 - 6000) * 0.10 + (18000 - 12000) * 0.20 + (25000 - 18000) * 0.30 + (income_int - 25000) * 0.40
elif income_int <= 50000:
    taxes = (12000 - 6000) * 0.10 + (18000 - 12000) * 0.20 + (25000 - 18000) * 0.30 + (35000 - 25000) * 0.40 + (income_int - 35000) * 0.45
else:
    taxes = (12000 - 6000) * 0.10 + (18000 - 12000) * 0.20 + (25000 - 18000) * 0.30 + (35000 - 25000) * 0.40 + (50000 - 35000) * 0.45 + (income_int - 50000) * 0.51
print("taxes:", taxes)

# 11 V
age_11: int = int(input("Enter age: "))
height_11: int = int(input("Enter height (cm): "))
if 18 > age_11 > 8 and height_11 > 115 or age_11 > 18 and height_11 > 100:
    print("You are allowed to enter the roller coaster!")
else:
    print("You are NOT allowed to enter the roller coaster!")


# loops

# 1 V
top_1: int = int(input("Enter a positive int: "))
for num in range(1, top_1 + 1):
    print(num, end=" ")

# 2 V
loop_x_2: int = int(input("Enter first number: "))
loop_y_2: int = int(input("Enter second number: "))
if loop_x_2 > loop_y_2:
    for num in range(loop_y_2, loop_x_2 + 1):
        print(num, end=" ")
else:
    for num in range(loop_x_2, loop_y_2 + 1):
        print(num, end=" ")

# 3 V
n_3: int = int(input("Enter a positive int: "))
for num in range(n_3 + 1):
    if num % 2 == 0:
        print(num, end=" ")

# 4 V
max_4: int = int(input("Enter the max: "))
den: int = int(input("Enter the den: "))
for num in range(max_4 + 1):
    if num % den == 0:
        print(num, end=" ")

# data processing

# 1 V
process_1_sum = 0
while True:
    process_1_user_input: int = int(input("Enter a number(-99 to exit): "))
    if process_1_user_input == -99:
        print(None if process_1_sum == 0 else process_1_sum)
        break
    process_1_sum = process_1_sum + process_1_user_input

# 2 V
process_2_max_num: int = 0
process_2_min_num: int = 999999999999999999999999999999999999999999
while True:
    process_2_user_input: int = int(input("Enter a number (negative or 0 to exit): "))
    if process_2_user_input <= 0:
        print("min", None if process_2_max_num == 0 else process_2_max_num)
        print("max", None if process_2_min_num == 999999999999999999999999999999999999999999 else process_2_min_num)
        break
    if process_2_user_input > process_2_max_num:
        process_2_max_num = process_2_user_input
    if process_2_user_input < process_2_min_num:
        process_2_min_num = process_2_user_input


# 3 V
process_3_1: int = int(input("Enter a num: "))
process_3_max_num = "1"
process_3_2: int = int(input("Enter a num: "))
if process_3_2 > process_3_1:
    process_3_max_num = "2"
process_3_3: int = int(input("Enter a num: "))
if process_3_3 > process_3_2:
    process_3_max_num = "3"
process_3_4: int = int(input("Enter a num: "))
if process_3_4 > process_3_3:
    process_3_max_num = "4"
process_3_5: int = int(input("Enter a num: "))
if process_3_5 > process_3_4:
    process_3_max_num = "5"
print(process_3_max_num)

# 4 V
process_4_x: int = int(input("Enter first number: "))
process_4_y: int = int(input("Enter second number: "))
process_4result: int = 0
for _ in range(process_4_x):
    process_4result = process_4result + process_4_y
print(process_4result)

# 5 V
process_5_x: int = int(input("Enter first number: "))
process_5_y: int = int(input("Enter second number: "))
process_5_result: int = process_5_x
for _ in range(process_5_y - 1):
    process_5_result = process_5_result * process_5_x
print(process_5_result)

# 6 bonus V
process_6_int: int = int(input("Enter a num: "))
process_6_digit: int = int(input("Enter a digit: "))
found: bool = False
while process_6_int > 0:
        current_digit = process_6_int % 10
        if current_digit == process_6_digit:
            found = True
            break
        process_6_int = process_6_int // 10
print("True" if found else "False")

# 7 bonus V
process_7_x = int(input("Enter the first number: "))
process_7_y = int(input("Enter the second number: "))
biggest_div = 1
if process_7_x < process_7_y:
    process_7_smallest_num = process_7_x
else:
    process_7_smallest_num = process_7_y

for i in range(process_7_smallest_num, 0, -1):
    if process_7_x % i == 0 and process_7_y % i == 0:
        biggest_div = i
        break

print("The greatest common divisor is:", biggest_div)

# 8
process_8_num: int = int(input("Enter a num to check if rishoni: "))
for i in range(2, process_8_num):
    if process_8_num % i == 0:
        print("Lo rishoni")
        break
else:
    print("Rishoni")

# Complex loops

# 1 V
temp_list: list[int] = []
cards = 12
while cards > 0:
    print(cards)
    try:
        card_input = int(input("Enter temp: "))
    except ValueError:
        print("Enter a number.")
        continue

    if -5 < card_input < 40:
        if card_input == 0 and temp_list[-1] == 0:
                print("two zeros in a row that's a mistake, try again...")
                continue
        else:
            #print("correct data")
            temp_list.append(card_input)
            cards = cards - 1
    else:
        print("wrong data")
        break
print(f"average temps: {sum(temp_list) / 12}, min- {min(temp_list)}, max- {max(temp_list)}")

# 2 V
countries: int = 44
countries_list: list[int] = []
while countries > 0:
    #print(countries)
    try:
        oom_input = int(input("Enter your vote (1-4): "))
    except ValueError:
        print("Enter a number between 1-4.")
        continue
    match oom_input:
        case 1:
            countries_list.append(1)
            countries -= 1
        case 2:
            countries_list.append(2)
            countries -= 1
        case 3:
            countries_list.append(3)
            countries -= 1
        case 4:
            countries_list.append(4)
            print("the country that veto'ed is country number: ", countries_list.index(4) + 1)
            break
print(f"voted yes: {countries_list.count(1)}, voted no: {countries_list.count(2)}, voted objected: {countries_list.count(3)}")
try:
    print(f"first voted yes: {countries_list.index(1) + 1}")
except:
    pass
try:
    print(f"first voted no: {countries_list.index(2) + 1}")
except:
    pass
