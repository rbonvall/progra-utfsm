m = int(raw_input('m: '))
cuenta = 0
for n in range(m):
    c = 0
    for d in range(1, n + 1):
        if n % d == 0:
            c += 1
    if c == 2:
        cuenta += 1
print 'Hay', cuenta, 'primos menores que', m
