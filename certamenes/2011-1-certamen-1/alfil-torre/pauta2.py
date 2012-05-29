fa = int(raw_input('Fila alfil: '))
ca = int(raw_input('Columna alfil: '))
ft = int(raw_input('Fila torre: '))
ct = int(raw_input('Columna torre: '))

if fa == ft or ca == ct:
    print 'Torre captura'
elif fa + ca == ft + ct or fa - ca == ft - ct:
    print 'Alfil captura'
else:
    print 'Ninguno captura'
