bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
print('all bool1', bool1, all(bool1))  # true
print('all bool2', bool2, all(bool2))  # false
print('all bool3', bool3, all(bool3))  # false

bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
bool4: list[bool] = [False, False]
bool5: list[int] = [0, 0, 0, 0, 0]
print('any bool1', bool1, any(bool1))  # true
print('any bool2', bool2, any(bool2))  # true
print('any bool3', bool3, any(bool3))  # true
print('any bool4', bool4, any(bool4))  # false
print('any bool5', bool5, any(bool5))  # false