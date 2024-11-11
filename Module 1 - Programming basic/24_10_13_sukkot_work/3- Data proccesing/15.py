# 15
input_num1: int = int(input("Enter num 1: "))
input_num2: int = int(input("Enter num 2: "))
counter: int = 0
while input_num1 > 0:
    counter = counter - 1 # had to use subtraction...
    input_num1 = input_num1 - input_num2
print(f"Answer is {-counter}") # converting it back to positive number :)