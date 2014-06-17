tamanos = {
  'Portaaviones': 5,
  'Acorazado': 4,
  'Submarino': 3,
  'Crucero': 2,
}

nombre = raw_input('Archivo de barcos: ')
nuevo = 'tablero-' + nombre

entrada = open(nombre)
casillas = set()
for linea in entrada:
    datos = linea.split()
    barco, fila, columna, direccion = linea.split()
    fila, columna = int(fila), int(columna)
    for i in range(tamanos[barco]):
        if direccion == 'H':
            casillas.add((fila, columna + i))
        else:
            casillas.add((fila + i, columna))
entrada.close()

salida = open(nuevo, 'w')
salida.write('  ')
for i in range(10):
    salida.write(str(i) + ' ')
salida.write('\n')
for i in range(10):
    salida.write(str(i) + ' ')
    for j in range(10):
        if (i, j) in casillas:
            salida.write('# ')
        else:
            salida.write('. ')
    salida.write('\n')
salida.close()

print 'Se ha creado el archivo', nuevo

