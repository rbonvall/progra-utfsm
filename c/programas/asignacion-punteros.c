#include <stdio.h>

int main() {
    int a, b;
    float z;
    int *x;
    int *y;

    a = 1;
    b = 2;
    z = 6.02e23;

    x = NULL;   /* valido */
    x = &a;     /* valido */
    x = &b;     /* valido */
/*  x = &z;        invalido (z no es un entero) */
/*  x = 142857;    invalido (142857 no es una dirección de memoria) */

    y = &b;     /* valido */
    y = x;      /* valido */
    y = NULL;   /* valido */
/*  y = &x;        invalido (x no es un entero) */

    printf("%d %d %f %p %p\n", a, b, z, x, y);

    return 0;
}
