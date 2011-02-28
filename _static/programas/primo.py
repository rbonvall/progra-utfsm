n = int(raw_input('Ingrese n: '))
es_primo = True
for d in range(2, n):
    if n % d == 0:
        es_primo = False
if es_primo:
    print n, 'es primo'
else:
    print n, 'es compuesto'
