'''
# CASO 1
Palabra? `perro`
Definicion: animal de cuatro patas.
La palabra es un sustantivo.
# FIN CASO 1

# CASO 2
Palabra? `silla`
La palabra no esta en el diccionario
# FIN CASO 2
'''

palabra_por_buscar = raw_input('Palabra? ')

archivo = open('diccionario.txt')

encontrada = False
for linea in archivo:
    izq, definicion = linea.split(':')
    palabra, tipo = izq.split()
    if palabra_por_buscar == palabra:
        encontrada = True
        print 'Definicion:', definicion.strip()
        if tipo[1] == 's':
            print 'La palabra es un sustantivo.'
        else:
            print 'La palabra es un verbo.'
        break

if not encontrada:
    print 'La palabra no esta en el diccionario'

archivo.close()

