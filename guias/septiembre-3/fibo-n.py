n = int(raw_input('Ingrese n: '))
print 'Los primeros', n, 'numeros de Fibonacci son:'

anterior = 0
actual = 1

print 0
for i in range(n - 1):
    print actual
    suma = anterior + actual
    anterior = actual
    actual = suma

