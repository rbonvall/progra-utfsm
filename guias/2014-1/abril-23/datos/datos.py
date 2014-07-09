from math import sqrt

def promedio(valores):
    return float(sum(valores)) / len(valores)

def desviacion(valores):
    p = promedio(valores)
    s = 0.0
    for x in valores:
        s += (x - p) ** 2
    return sqrt(s / len(valores))

def mediana(valores):
    ordenados = sorted(valores)
    n = len(valores)
    return ordenados[n / 2]


n = int(raw_input('Cuantos datos? '))
datos = []
for i in range(n):
    x = float(raw_input('Dato ' + str(i + 1) + ': '))
    datos.append(x)

print 'El promedio es', promedio(datos)
print 'La desviacion estandar es', desviacion(datos)
print 'La mediana es', mediana(datos)
