# 11
minuses_sum: int = 0
while True:
    x = int(input("Enter a number: "))
    if x < 0:
        minuses_sum = minuses_sum + x
    if x == 0:
        print(minuses_sum)
        break