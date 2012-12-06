m = int(raw_input('Ingrese m: '))

anterior = 0
actual = 1

while actual < m:
    suma = anterior + actual
    anterior = actual
    actual = suma

if actual == m:
    print m, 'es un numero de Fibonacci'
else:
    print m, 'no es un numero de Fibonacci'
