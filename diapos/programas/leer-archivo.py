archivo = open('quijote.txt')
for linea in archivo:
    print linea.strip().upper()
archivo.close()
