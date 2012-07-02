'''
# CASO 1
>>> convertir_csv_a_html("frutas")

# FIN CASO 1

# CASO 2
>>> buscar_valor("frutas", "Kiwi")
3
>>> buscar_valor("frutas", "Naranja")
None

# FIN CASO 2
'''

def convertir_csv_a_html(tabla):
    archivo_csv  = open(tabla + '.csv')
    archivo_html = open(tabla + '.html', 'w')

    archivo_html.write('<table>\n')
    for linea in archivo_csv:
        archivo_html.write('<tr>\n')
        valores = linea.split()
        for valor in valores:
            archivo_html.write('<td>{0}</td>\n'.format(valor))
        archivo_html.write('</tr>\n')
    archivo_html.write('</table>')

    archivo_csv.close()
    archivo_html.close()

