palabra = raw_input('Palabra: ')
n = len(palabra)
cuenta = 0
for i in range(n):
    letra = palabra[i]
    if letra in 'aeiou':
        cuenta += 1
print cuenta, 'vocales'
