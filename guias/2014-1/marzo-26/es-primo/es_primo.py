n = int(raw_input('n: '))
c = 0
for d in range(1, n + 1):
    if n % d == 0:
        c += 1
if c == 2:
    print 'Es primo'
else:
    print 'No es primo'

