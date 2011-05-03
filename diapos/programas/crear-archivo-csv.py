archivo = open('alumnos.txt', 'w')

# ...

linea = ':'.join(valores) + '\n'
archivo.write(linea)

# ...

archivo.close()
