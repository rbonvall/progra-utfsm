peor = 100
mejor = 0
suma = 0.0
n = int(raw_input('Cuantas notas? '))
for i in range(n):
    nota = int(raw_input('Nota: '))
    suma += nota
    mejor = max(mejor, nota)
    peor = min(peor, nota)
nf = (suma  - mejor - peor) / (n - 2)
print 'Nota final: ', nf


