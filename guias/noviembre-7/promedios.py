archivo = open('curso.txt')

plantilla = '{:20} {:>4} {:10}'

print '-' * 37
print plantilla.format('Estudiante', 'Nota', 'Situacion')
print '-' * 37

for linea in archivo:
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
    print mensaje

archivo.close()

