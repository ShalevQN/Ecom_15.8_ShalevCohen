def mul_range(num1, num2):
    if num1 == num2:
        return num1
    else:
        return num1 * mul_range(num1 + 1, num2)
