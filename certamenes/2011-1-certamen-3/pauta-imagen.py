from numpy import *

def reducir(img, f):
    M, N = img.shape
    m, n = M / f, N / f
    nueva = zeros((m, n)).astype(int)
    for i in range(m):
        for j in range(n):
            promedio = img[f * i : f * (i + 1),
                           f * j : f * (j + 1)].mean().astype(int)
            nueva[i, j] = promedio
    return nueva

def binarizar(img, umbral):
    return 255 * (img >= umbral)

if __name__ == '__main__':
    img = arange(12 * 18).reshape((12, 18))
    print img
    print reducir(img, 2)
    print reducir(img, 3)
    print binarizar(img, 80)
    print binarizar(img, 160)

