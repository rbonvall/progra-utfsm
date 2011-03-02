p = raw_input('Palabra 1: ')
q = raw_input('Palabra 2: ')

largo_p = len(p)
largo_q = len(q)

iguales1 = p[largo_p - 1] == q[largo_q - 1]
iguales2 = p[largo_p - 2] == q[largo_q - 2]
iguales3 = p[largo_p - 3] == q[largo_q - 3]
iguales4 = p[largo_p - 4] == q[largo_q - 4]

print (iguales1 and iguales2 and
       iguales3 and iguales4)

