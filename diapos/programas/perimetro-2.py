def distancia(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = x2 - x1, y2 - y1
    return (dx ** 2 + dy ** 2) ** .5

def perimetro(vertices):
    n = len(vertices)
    actual = vertices[0:n]
    sgte = vertices[1:n] + [vertices[0]]

    distancias = []
    for i in range(n):
        d = distancia(actual[i], sgte[i])
        distancias.append(d)
    return sum(distancias)

