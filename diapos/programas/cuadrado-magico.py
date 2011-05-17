from numpy import *


def es_magico(a):
    # obtener las dimensiones del arreglo
    m, n = a.shape

    # obtener la suma de la primera fila como referencia
    total = sum(a[0, :])

    # verificar las sumas de todas las filas
    for i in range(m):
        if sum(a[i, :]) != total:
            return False

    # verificar las sumas de todas las columnas
    for j in range(n):
        if sum(a[:, j]) != total:
            return False

    # verificar suma de la diagonal
    if sum(diag(a)) != total:
        return False

    # La antidiagonal es la parte dificil,
    # ya que no hay una funcion para obtenerla directamente.

    # Una solucion es sumar elemento a elemento usando un ciclo:
    # (como se haria en C o Pascal):
    s = 0
    for i in range(m):
        s = s + a[i, n - i - 1]
    if s != total:
        return False

    # Otra solucion es invertir el orden de las filas
    # y sacar la diagonal:
    antidiagonal = diag(a[::-1, :])
    if sum(antidiagonal) != total:
        return False

    # Una tercera solucion es usar un arreglo de indices:
    antidiagonal = a[arange(m), arange(n - 1, -1, -1)]
    if sum(antidiagonal) != total:
        return False

    return True


# misma funcion, version completamente iterativa
def es_magico(a):
    m, n = a.shape

    total = 0
    for i in range(m):
        total += a[i, 0]

    sumas_filas = zeros(m)
    sumas_columnas = zeros(m)
    suma_diagonal = 0
    suma_antidiagonal = 0

    for i in range(m):
        for j in range(n):
            sumas_filas[i] += a[i, j]
            sumas_columnas[j] += a[i, j]
        suma_diagonal += a[i, i]
        suma_antidiagonal += a[i, n - i - 1]

    return (all(sumas_filas == total) and
            all(sumas_columnas == total) and
            suma_diagonal == suma_antidiagonal == total)



if __name__ == '__main__':

    # cuadrado magico
    a = array([[ 4, 15, 14,  1],
               [ 9,  6,  7, 12],
               [ 5, 10, 11,  8],
               [16,  3,  2, 13]])

    # cuadrado no magico
    b = array([[16,  3,  7, 11],
               [ 6,  2, 10,  4],
               [13,  9,  1, 15],
               [14,  5,  8, 12]])

    print 'a:', es_magico(a)
    print 'b:', es_magico(b)
