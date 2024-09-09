
# MAKE ALL OF THESE CONDITIONS FALSE

a = 1
b = 0
if a == b: # don't need to change anything, a!=b which goes to else.
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
d = 0
if a + b and c + d: # I don't get these statements, please explain next lesson.
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 3
c = 0
d = 0
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 2
b = 3
c = 0
d = 0
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 0
c = 0
d = 0
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d: # still, I don't get these statement...
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
if a != b: # don't need to change anything, a=b, they're both 0.
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or True: # Unsolvable, "or True" always results in True.
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 1
b = 0
c = 0
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 3
b = 2
c = 2
d = 2
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")