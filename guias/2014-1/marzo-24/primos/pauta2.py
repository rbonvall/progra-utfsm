cuantos = int(raw_input('Cantidad de primos: '))
n = 2
c = 0
while c < cuantos:
    es_primo = True
    for d in range(2, n):
        if n % d == 0:
            es_primo = False
            break

    if es_primo:
        print n,
        c += 1
    n += 1

