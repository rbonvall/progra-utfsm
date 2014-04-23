def segundo(lista):
    return lista[1]

def divisores(n):
    d = []
    for i in range(1, n + 1):
        if n % i == 0:
            d.append(i)
    return d

def promedio(valores):
    return float(sum(valores)) / len(valores)

def contar_mayores_que(m, lista):
    c = 0
    for x in lista:
        if x > m:
            c += 1
    return c

def emparejar(valores):
    parejas = []
    for i in range(len(valores) / 2):
        p = [valores[2 * i], valores[2 * i + 1]]
        parejas.append(p)
    return parejas

def emparejar2(valores):
    parejas = []
    p = []
    for x in valores:
        p.append(x)
        if len(p) == 2:
            parejas.append(p)
            p = []
    return parejas
