archivo = open('quijote.txt')
c_letras = 0
c_palabras = 0
c_lineas = 0
for linea in archivo:
    palabras = linea.strip().split()
    letras = linea.strip().replace(' ', '')

    c_letras = c_letras + len(letras)
    c_palabras = c_palabras + len(palabras)
    c_lineas = c_lineas + 1

print 'El archivo tiene',
print '{0} letras, {1} palabras y {2} lineas'.format(c_letras, c_palabras, c_lineas)
