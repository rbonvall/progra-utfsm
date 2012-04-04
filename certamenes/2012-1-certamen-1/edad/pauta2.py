ano = int(raw_input('Ano: '))
mes = int(raw_input('Mes: '))
dia = int(raw_input('Dia: '))

if mes < 5 or (mes == 5 and dia < 10):
    edad_anos = 2012 - ano
else:
    edad_anos = 2011 - ano

if dia <= 10:
    edad_meses = (5 - mes) % 12
else:
    edad_meses = (4 - mes) % 12

edad_dias = (10 - dia) % 30


print 'Edad:',
print edad_anos,  'anos,',
print edad_meses, 'meses,',
print edad_dias,  'dias.'
