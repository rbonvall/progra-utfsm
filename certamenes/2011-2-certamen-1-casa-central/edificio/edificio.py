depto = int(raw_input('Departamento: '))
piso = depto / 100
posicion = depto % 100

if depto == 807:
    precio = 500
elif piso == 1:
    precio = 100
elif piso == 25:
    precio = 400
elif 2 <= piso <= 24:
    precio = 245
    if posicion == 3 or posicion == 7:   # tambien puede ser posicion % 4 == 3
        precio = int(precio * 1.13)
    elif posicion == 0 or posicion == 4: # tambien puede ser posicion % 4 == 0
        precio = int(precio * 0.83)

print 'El precio es', precio



