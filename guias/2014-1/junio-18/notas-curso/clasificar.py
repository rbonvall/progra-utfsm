entrada = open('curso.txt')
aprobados = open('aprobados.txt', 'w')
reprobados = open('reprobados.txt', 'w')

for linea in entrada:
    datos = linea.split(':')
    nombre, apellido = datos[0:2]
    anno, mes, dia = map(int, datos[2].split('/'))
    notas = map(float, datos[3:])

    promedio = int(round(sum(notas) / len(notas)))

    plantilla = '{0}:{1}:{2}\n'
    mensaje = plantilla.format(nombre, apellido, promedio)

    if promedio < 55:
        reprobados.write(mensaje)
    else:
        aprobados.write(mensaje)

entrada.close()
aprobados.close()
reprobados.close()

