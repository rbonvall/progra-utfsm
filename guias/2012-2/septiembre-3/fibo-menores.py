m = int(raw_input('Ingrese m: '))
print 'Los numeros de Fibonacci menores que', m, 'son:'

anterior = 0
actual = 1

print 0
while actual < m:
    print actual
    suma = anterior + actual
    anterior = actual
    actual = suma

