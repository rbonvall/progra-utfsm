def es_primo(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return n > 1

def factores(n):
    f = []
    for d in range(1, n + 1):
        if n % d == 0:
            f.append(d)
    return f

def es_palindromo(n):
    s = str(n)
    return s == s[::-1]

def digitos(n):
    return map(int, str(n))

#n = 912673
#print n, 'primo:', es_primo(n)
#print 'Factores:', factores(n)
#print
#
#c = 0
#n = 1
#M = 3000
#while c < M:
#    n += 1
#    if es_primo(n):
#        c += 1
#print M, '-esimo primo:', n
#print
#
#M = 10000
#c = 0
#for i in range(2, M):
#    if es_primo(i):
#        c += 1
#print c, 'primos menores que', M
#print
#
#c = 0
#M = 30
#i = 2
#while c < M:
#    if es_palindromo(i):
#        if es_primo(i):
#            print i
#            c += 1
#    i += 1
#print

#p = 1
#c = 0
#n = 10
#i = 3
#d = 3
#while c < n:
#    if es_primo(i) and i % 10 == d:
#        p *= i
#        c += 1
#        print '\t', i
#    i += 2
#print 'Producto de', n, 'primos terminados en', d, ':', p

#i = 3
#s = 34
#while True:
#    if es_primo(i) and sum(digitos(i)) == s:
#        break
#    i += 2
#print 'Primo cuyos digitos suman {0}: {1}'.format(s, i)

desde = 10002
hasta = 60000
c = 0
for i in range(desde, hasta, 6):
    if es_primo(i - 1) and es_primo(i + 1):
        c += 1
print c, 'primos gemelos entre', desde, 'y', hasta


