def check_negative(num):
    return True if num > 0 else False



# print(check_negative(-5))
# print(check_negative(3))
# print(check_negative(0))


check_negative_lm = lambda num: num < 0

# print(check_negative_lm(-5))
# print(check_negative_lm(3))
# print(check_negative_lm(0))





def power(num):
    return num ** 2

print(power(3))

power_lm = lambda num: num ** 2

print(power_lm(3))