m = int(raw_input('m: '))
print 'Los primos menores que', m, 'son:'
for n in range(m):
    c = 0
    for d in range(1, n + 1):
        if n % d == 0:
            c += 1
    if c == 2:
        print n,
