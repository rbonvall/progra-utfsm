n = int(raw_input('n: '))
es_primo = n > 1
for d in range(2, n):
    if n % d == 0:
        es_primo = False
        break

if es_primo:
    print 'Primo'
else:
    print 'No primo'

