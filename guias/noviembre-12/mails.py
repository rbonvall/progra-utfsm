from os import makedirs

entrada = open('progra.txt')
makedirs('emails')

for linea in entrada:
    datos = linea.split(':')
    nombre, apellido, sexo = datos[0:3]
    anno, mes, dia = map(int, datos[3].split('/'))
    notas = map(float, datos[4].split(','))
    promedio = int(round(sum(notas) / len(notas)))

    direccion = '{0}.{1}@uvxyz.cl'.format(nombre[0], apellido)
    direccion = direccion.replace(' ', '').lower()

    nombre_archivo = (nombre + '-' + apellido).replace(' ', '-')

    if sexo == 'F':
        saludo = 'Estimada'
    else:
        saludo = 'Estimado'

    if promedio < 55:
        estado = 'reprobado'
    else:
        estado = 'aprobado'

    if promedio < 35:
        carita = ":'("
    elif promedio < 55:
        carita = ':('
    elif promedio < 85:
        carita = ':)'
    else:
        carita = ':D'

    email = open('emails/{0}.txt'.format(nombre_archivo), 'w')
    email.write('De: Rogelio Bombal <r.bombal@uvxyz.cl>\n')
    email.write('Para: {} {} <{}>\n\n'.format(nombre, apellido, direccion))
    email.write('{} {},\n'.format(saludo, nombre))
    email.write('le informamos que usted ha {} '.format(estado))
    email.write('con nota final {} {}\n\n'.format(promedio, carita))
    email.write('Saludos,\n')
    email.write('Rogelio Bombal.')
    email.close()

entrada.close()


