archivo = open('alumnos.txt')
for linea in archivo:
    valores = linea.strip().split(':')
    nombres = valores[0:2]
    notas = map(int, valores[2:5])
    print nombres[0], notas
archivo.close()
