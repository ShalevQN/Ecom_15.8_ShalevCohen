

#print(f"{"you are tall" if float(input("enter a height between 0.1-2.8: ")) > 1.8 else "you are not tall"}")

print(f"{"The number is one digit" if int(input("Enter a number between 0-99: " )) < 10 else "The number is two digits"}")





# enter num
num: int = int(input("Enter num: "))

# calculate the sum of every digit in the num
sum_digits: int = 0

while num > 0:
    sum_digits = sum_digits + (num % 10)
    num = num // 10
print(sum_digits)