# Entrada
n = int(raw_input('n: '))

# Proceso
f = 1
for i in range(n):
    f *= i + 1

# Salida
print 'n! =', f
