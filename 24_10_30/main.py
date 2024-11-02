# b
from my_func import print_stars

for _ in range(5):
    print_stars() # ii

print("---------")

import my_func
for _ in range(5):
    my_func.print_stars() # i

help(print_stars) # d