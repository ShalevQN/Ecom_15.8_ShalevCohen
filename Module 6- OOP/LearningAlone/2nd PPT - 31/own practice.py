def sum_of_digits(num):
    if num == 0:
        return num
    else:
        return num % 10 + sum_of_digits(num // 10)

print(sum_of_digits(1234))