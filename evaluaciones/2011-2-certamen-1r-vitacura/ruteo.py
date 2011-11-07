a = 11
b = a / 3
c = a / 2
n = 0

while a == b + c:
    n += 1
    b += c
    c = b - c
    if n % 2 == 0:
        a = 2 * a - 3
    print 100 * b + c

