a = True
b = '1'
c = 2
while b[-1] not in '378':
    a = 0 == len(b) % 2
    if a:
        c = c * 7
    b = b + str(c)
print c


