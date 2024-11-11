# 16
num: int = int(input("Enter a three digit number: "))
sum_digits: int = 0
while num > 0:
    sum_digits = sum_digits + (num % 10)
    num = num // 10
print(f"{sum_digits}is divisible by 3" if sum_digits % 3 ==0 else f"{sum_digits} is not divisible by 3")