import random

set1: set = {"1", "2", "3", "4", "5", "6", "7", "8"}

print(set1.pop())
print(set1)
set1.remove(random.choice(list(set1)))
print(set1)

