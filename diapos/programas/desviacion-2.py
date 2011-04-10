def leer_datos(cantidad):
    datos = []
    for i in range(1, cantidad + 1):
        x = float(raw_input('Dato ' + str(i) + ': '))
        datos.append(x)
    return datos

def promedio(valores):
    suma = 0.0
    for x in valores:
        suma += x
    return suma / len(valores)

def desviacion(valores):
    p = promedio(valores)
    n = len(valores)
    suma = 0.0
    for x in valores:
        suma += (x - p) ** 2
    return (suma / (n - 1)) ** 0.5

n = int(raw_input('Cuantos datos? '))
datos = leer_datos(n)
d = desviacion(datos)
print 'La desviacion estandar es', d


