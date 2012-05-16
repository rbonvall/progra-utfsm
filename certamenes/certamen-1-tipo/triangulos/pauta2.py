a = float(raw_input('Ingrese a: '))
b = float(raw_input('Ingrese b: '))
c = float(raw_input('Ingrese c: '))

if a > b + c or b > a + c or c > a + b:
    print 'No es un triangulo valido'
elif a == b == c:
    print 'El triangulo es equilatero'
elif a == b or b == c or a == c:
    print 'El triangulo es isoceles'
else:
    print 'El triangulo es escaleno'
