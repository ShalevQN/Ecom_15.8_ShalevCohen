
# MAKE ALL OF THESE CONDITIONS TRUE

a = 1
b = 1
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 1
b = 4
c = 3
d = 2
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if a >= b or c > d: # don't need to change anything, a=b they're both 0.
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if a >= b or c < d: # don't need to change anything, a=b they're both 0.
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if a == b and c <= d: # don't need to change anything, a=b and c=d, they're all 0.
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 1
c = 1
d = 1
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 1
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or True: # don't need to change anything, a=b is the only statement needed, both are 0.
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or False: # don't need to change anything, a=b is the only statement needed, both are 0.
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 4
b = 2
c = 4
d = 3
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")