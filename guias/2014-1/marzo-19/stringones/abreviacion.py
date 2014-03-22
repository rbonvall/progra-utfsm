abreviado = raw_input()
original = ''
n = len(abreviado)
for i in range(n / 2):
    cuenta = int(abreviado[2 * i])
    letra = abreviado[2 * i + 1]
    original += cuenta * letra
print original
