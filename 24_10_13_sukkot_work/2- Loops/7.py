# 7
for x in range(int(input("Enter a num: ")), int(input("Enter a second num: ")) + 1):
    if x % 2 == 0:
        print(x, end=" ")

# Comprehended:
# print([x for x in range(int(input("Enter a num: ")), int(input("Enter a second num: ")) + 1) if x % 2 == 0])