
counter: int = 10


def inc_counter(x):
    x = x + 1
    return x

def dec_counter(x):
    x = x - 1
    return x

def print_counter(x):
    print(x)



counter = inc_counter(counter)
counter = inc_counter(counter)
counter = inc_counter(counter)

counter = dec_counter(counter)
counter = dec_counter(counter)

print_counter(counter)



