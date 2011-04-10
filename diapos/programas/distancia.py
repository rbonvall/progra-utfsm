def distancia(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    return (dx ** 2 + dy ** 2 + dz ** 2) ** .5
