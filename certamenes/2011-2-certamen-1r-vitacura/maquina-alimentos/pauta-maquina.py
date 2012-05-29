producto = raw_input('Elija producto: ')
if producto == 'A':
    precio = 270
elif producto == 'B':
    precio = 340
elif producto == 'C':
    precio = 390

pagado = 0
print 'Ingrese monedas:'
while pagado < precio:
    moneda = int(raw_input())
    pagado += moneda

vuelto = pagado - precio
if vuelto > 0:
    print 'Su vuelto:'
    # es imposible pasarse por 100 o mas pesos
    for i in range(vuelto / 50):
        print 50
    vuelto %= 50
    for i in range(vuelto / 10):
        print 10

