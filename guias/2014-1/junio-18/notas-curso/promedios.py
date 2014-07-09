entrada = open('curso.txt')
salida  = open('promedios.txt', 'w')

plantilla = '{0:20} {1:>4} {2}\n'

salida.write(plantilla.format('Estudiante', 'Nota', 'Situacion'))
salida.write('-' * 35 + '\n')

for linea in entrada:
    datos = linea.split(':')
    nombre, apellido = datos[0:2]
    anno, mes, dia = map(int, datos[2].split('/'))
    notas = map(float, datos[3:])

    nombre_completo = nombre + ' ' + apellido
    email = (nombre[0] + apellido.replace(' ', '')).lower() + '@usm.cl'
    promedio = int(round(sum(notas) / len(notas)))

    if promedio < 55:
        estado = 'reprobado'
    else:
        estado = 'aprobado'

    mensaje = plantilla.format(nombre_completo, promedio, estado)
    salida.write(mensaje)

entrada.close()
salida.close()

