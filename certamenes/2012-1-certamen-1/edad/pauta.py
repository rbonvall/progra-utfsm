anno = int(raw_input('Anno: '))
mes  = int(raw_input('Mes: '))
dia  = int(raw_input('Dia: '))

if mes < 5 or (mes == 5 and dia < 10):
    edad_annos = 2011 - anno
else:
    edad_annos = 2012 - anno

print edad_annos, 'annos,',
print edad_meses, 'meses,',
print edad_dias,  'dias.'
