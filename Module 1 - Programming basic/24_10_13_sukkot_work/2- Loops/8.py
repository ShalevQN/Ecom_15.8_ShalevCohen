# 8
for x in range(1 , int(input("Enter a num: ")) + 1):
    if x % 3 == 0 or x % 5 == 0:
        print(x, end=" ")

# Comprehended:
# print([x for x in range(1 , int(input("Enter a num: ")) + 1) if x % 3 == 0 or x % 5 == 0])