'''
# CASO
Que dia es? `martes`
Mate 1-2
Fisica 7-8
Quimica 5-6
# FIN CASO
'''

hoy = raw_input('Que dia es? ')
hoy = hoy[:2]

archivo = open('horario.txt')
for linea in archivo:
    ramo, clases = linea.split(': ')
    lista_clases = clases.split(', ')
    for clase in lista_clases:
        dia, bloque = clase.split()
        if dia == hoy:
            print ramo, bloque

archivo.close()


