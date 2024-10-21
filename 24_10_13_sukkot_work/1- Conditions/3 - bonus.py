# 3 - bonus
remainder_float1: float = (float(input("Enter a num: ")) * 10) % 10
remainder_float2: float = (float(input("Enter a num: ")) * 10) % 10

print(remainder_float1 / 10 if remainder_float1 > remainder_float2 else "Even" if remainder_float1 == remainder_float2 else remainder_float2 / 10)