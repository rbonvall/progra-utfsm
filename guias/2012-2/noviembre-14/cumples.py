entrada = open('progra.txt')
pagina = open('cumples.html', 'w')

cabecera = '''\
<!doctype html>
<title>Cumplea&ntilde;os</title>
<h1>Cumplea&ntilde;os</h1>

'''

meses = ['',
    'Enero', 'Febrero', 'Marzo', 'Abril',
    'Mayo', 'Junio', 'Julio', 'Agosto',
    'Septiembre', 'Octubre', 'Noviembre', 'Diciembre',
]

estudiantes = []

for linea in entrada:
    datos = linea.split(':')
    nombre, apellido, sexo = datos[0:3]
    anno, mes, dia = map(int, datos[3].split('/'))
    notas = map(float, datos[4].split(','))
    nombre_completo = nombre + ' ' + apellido

    estudiantes.append((mes, dia, nombre_completo))

estudiantes.sort()

pagina.write(cabecera)
for m in range(1, 13):
    pagina.write('<h2>' + meses[m] + '</h2>\n')
    pagina.write('<ul>\n')
    for mes, dia, nombre_completo in estudiantes:
        if mes == m:
            pagina.write('  <li> <b>{0}:</b> {1}\n'.format(dia, nombre_completo))
    pagina.write('</ul>\n\n')

entrada.close()
pagina.close()



