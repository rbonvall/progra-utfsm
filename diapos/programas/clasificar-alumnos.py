archivo_alumnos = open('alumnos.txt')
archivo_aprobados = open('aprobados.txt', 'w')
archivo_reprobados = open('reprobados.txt', 'w')

for linea in archivo_alumnos:

    valores = linea.strip().split(':')

    nombre = valores[0]
    apellido = valores[1]
    notas = map(int, valores[2:5])
    promedio = int(round(sum(notas) / 3.0))

    linea = '{0},{1},{2}\n'.format(nombre, apellido, promedio)
    if promedio < 55:
        archivo_reprobados.write(linea)
    else:
        archivo_aprobados.write(linea)

archivo_alumnos.close()
archivo_aprobados.close()
archivo_reprobados.close()
