maximo = int(raw_input('Mostrar primos menores que: '))
for n in range(2, maximo):
    es_primo = True
    for d in range(2, n):
        if n % d == 0:
            es_primo = False
            break

    if es_primo:
        print n,

