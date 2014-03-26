m = int(raw_input('m: '))
print 'Los', m, 'primeros primos son:'
cuenta = 0
n = 2
while cuenta < m:
    c = 0
    for d in range(1, n + 1):
        if n % d == 0:
            c += 1
    if c == 2:
        print n,
        cuenta += 1
    n += 1
