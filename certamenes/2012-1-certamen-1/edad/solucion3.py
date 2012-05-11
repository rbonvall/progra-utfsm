ano = int(raw_input('Ano: '))
mes = int(raw_input('Mes: '))
dia = int(raw_input('Dia: '))

ya_tuvo_cumpleanos = mes < 5 or (mes == 5 and dia <= 10)
ya_tuvo_cumplemes = dia <= 10

edad_anos  = 2012 - ano - (not ya_tuvo_cumpleanos)
edad_meses =  ( 5 - mes - (not ya_tuvo_cumplemes)) % 12
edad_dias  =  (10 - dia) % 30

print 'Edad:',
print edad_anos,  'anos,',
print edad_meses, 'meses,',
print edad_dias,  'dias.'
