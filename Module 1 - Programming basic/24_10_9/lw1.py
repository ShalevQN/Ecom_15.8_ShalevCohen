# targil -- use any/all




# check if a list [True, False, False, True] contains at least 1 False
#   if yes -- print '1+ False' else print '0 False'

if not all([True, False, False, True]):
    print("1+ False")
else:
    print("0 False")



# check if a list [False, False, False, False] contains all False
#   if yes -- print 'All False' else print 'not All False'

if not any([False, False, False, False]):
    print("All False")
else:
    print("not All False")



# *Bonus: check if a list [3, 9, 12, 15, 16] contains only numbers divided by 3 no reminder
#   if yes -- print 'All 3 divided' else print 'not All3 divided'


if all(i % 3 == 0 for i in [3, 9, 12, 15, 16]):
    print("All divisible by 3")
else:
    print("Not all divisible by 3")


