def func1(x): # x → stack
    x = 'a' + x # new string in heap
    return x # returns string from heap

def func2(y): # y → stack
    y.append('c') # modifies list in heap
    return y # returns same list (heap)

def func3(z): # z → stack
    z['new_key'] = 'new value' # modifies dict in heap

if __name__ == '__main__':
    a = 'b' # a → stack, 'b' → heap
    b = func1(a) # b → stack, 'ab' → heap
    print(a, b) # b ab

    c = ['d', 'e'] # c → stack, list + items → heap
    d = func2(c) # d → stack, same list as c
    print(c, d) # ['d', 'e', 'c'] ['d', 'e', 'c']

    e = {'key': 'value'} # e → stack, dict + strings → heap
    f = func3(e) # f → stack, None; dict modified
    print(e, f) # {'key': 'value', 'new_key': 'new value'} None
