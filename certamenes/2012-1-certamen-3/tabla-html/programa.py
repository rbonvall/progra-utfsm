'''
# CASO 1
>>> convertir_csv_a_html("frutas")

# FIN CASO 1

# CASO 1b
>>> convertir_csv_a_html("test")

# FIN CASO 1b

# CASO 2
>>> obtener_tamano("frutas.html")
(3, 3)

# FIN CASO 2

# CASO 2b
>>> obtener_tamano("test.html")
(7, 5)

# FIN CASO 2b

# CASO 3
>>> obtener_precio("Kiwi")
471

# FIN CASO 3

# CASO 3b
>>> obtener_precio("Arandano")

# FIN CASO 3b
'''

def convertir_csv_a_html(tabla):
    archivo_csv  = open(tabla + '.csv')
    archivo_html = open(tabla + '.html', 'w')

    archivo_html.write('<table>\n')
    for linea in archivo_csv:
        archivo_html.write('<tr>\n')
        valores = linea.split(',')
        for valor in valores:
            archivo_html.write('<td>{0}</td>\n'.format(valor))
        archivo_html.write('</tr>\n')
    archivo_html.write('</table>')

    archivo_csv.close()
    archivo_html.close()

def obtener_tamano(archivo_html):
    n_filas = 0
    n_columnas = 0
    archivo = open(archivo_html)
    for linea in archivo:
        linea = linea.strip()        # por si acaso, pero no es necesario
        if linea == '<tr>':
            n_filas += 1
            n_columnas = 0
        elif linea[0:4] == '<td>':   # o tambien '<td>' in linea
            n_columnas += 1
    archivo.close()
    return (n_filas, n_columnas)

def obtener_precio(fruta):
    archivo = open('frutas.csv')
    precio = None
    for linea in archivo:
        f, _, p = linea.split(',')
        if f == fruta:
            precio = int(p.replace('$', ''))
            break
    archivo.close()
    return precio


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

