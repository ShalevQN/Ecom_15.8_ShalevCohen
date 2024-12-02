# fibbonachi:

def finding_fib_by_index(index):
    a = 1
    b = 1
    for _ in range(index):
        c = a + b
        a = b
        b = c
    else:
        return a

print(finding_fib_by_index(20))
