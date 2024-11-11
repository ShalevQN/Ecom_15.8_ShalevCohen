
counter: int = 10


def inc_counter():
    global counter
    counter = counter + 1

def dec_counter():
    global counter
    counter = counter - 1

def print_counter():
    print(counter)

def inc_local_counter():
    counter = 20


inc_counter()
inc_counter()
inc_counter()

dec_counter()
dec_counter()

print_counter()

inc_local_counter()

print_counter()



