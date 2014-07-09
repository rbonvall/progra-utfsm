m = int(raw_input('m: '))
suma = 0
cuenta = 0
n = 2
while cuenta < m:
    c = 0
    for d in range(1, n + 1):
        if n % d == 0:
            c += 1
    if c == 2:
        cuenta += 1
        suma += n
    n += 1
print 'La suma de los', m, 'primeros primos es', suma
