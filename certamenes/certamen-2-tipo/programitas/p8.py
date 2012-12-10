def f(a):
    if a == 0:
        return 1
    return a + f(a / 2)
print f(15)
