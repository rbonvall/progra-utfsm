#include <stdio.h>

int main() {
    float w, z;
    float *p, *q;

    w = 20;
    p = &z;
    q = p;
    *q = 7;
    z += *q;
    w -= *p;
    p = &w;
    *q += *p;
    z += *(&w);
    p = q;
    *p = *q;

    printf("%f %f %f %f\n", w, z, *p, *q);
    return 0;
}
