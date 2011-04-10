n = int(raw_input('Cuantos datos? '))

datos = []
for i in range(1, n + 1):
    x = float(raw_input('Dato ' + str(i) + ': '))
    datos.append(x)

suma = 0.0
for x in datos:
    suma = suma + x
promedio = suma / n

suma_dif_cuad = 0.0
for x in datos:
    suma_dif_cuad = suma_dif_cuad + (x - promedio) ** 2
desviacion = (suma_dif_cuad / (n - 1)) ** 0.5

print 'La desviacion estandar es', desviacion

