print 'Ingrese varios numeros'

n = 0
suma = 0.0
while suma < 10.0:
    x = float(raw_input())
    n = n + 1
    suma = suma + x

promedio = suma / n
print 'El promedio es', promedio
