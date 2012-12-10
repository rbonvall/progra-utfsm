entrada = open('progra.txt')
pagina = open('progra.html', 'w')

cabecera = '''\
<!doctype html>
<title>Lista del curso</title>
<h1>Lista del curso</h1>
<table>
'''

pie = '''\
</table>
'''

pagina.write(cabecera)
for linea in entrada:
    datos = linea.split(':')
    nombre, apellido, sexo = datos[0:3]
    anno, mes, dia = map(int, datos[3].split('/'))
    notas = map(float, datos[4].split(','))
    promedio = int(round(sum(notas) / len(notas)))

    pagina.write('  <tr>\n')
    pagina.write('    <td>{0}</td>\n'.format(nombre + ' ' + apellido))
    for i in range(5):
        pagina.write('    <td>{0}</td>\n'.format(int(notas[i])))
    pagina.write('    <td><b>{0}</b></td>\n'.format(promedio))
    pagina.write('  </tr>\n')

pagina.write(pie)

entrada.close()
pagina.close()



