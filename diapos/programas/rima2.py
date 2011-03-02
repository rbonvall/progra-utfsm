p = raw_input('Palabra 1: ')
q = raw_input('Palabra 2: ')

iguales1 = p[-1] == q[-1]
iguales2 = p[-2] == q[-2]
iguales3 = p[-3] == q[-3]
iguales4 = p[-4] == q[-4]

print (iguales1 and iguales2 and
       iguales3 and iguales4)

