ano = int(raw_input('Ano: '))
mes = int(raw_input('Mes: '))
dia = int(raw_input('Dia: '))

hoy =  10 + 30 * 4         + 30 * 12 * 2012
nac = dia + 30 * (mes - 1) + 30 * 12 * ano

tiempo = hoy - nac
edad_anos  = tiempo / (12 * 30)
edad_meses = tiempo % (12 * 30) / 30
edad_dias  = tiempo % 30

print 'Edad:',
print edad_anos,  'anos,',
print edad_meses, 'meses,',
print edad_dias,  'dias.'
