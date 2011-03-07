n = int(raw_input('Cuantos numeros? '))

suma = 0.0
for i in range(n):
    x = float(raw_input())
    suma = suma + x

promedio = suma / n
print 'El promedio es', promedio
