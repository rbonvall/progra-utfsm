#include <stdio.h>

struct fecha {
    int anno;
    int mes;
    int dia;
};

int main() {
    int n = 10;
    char c = '\n';
    float x = 3.14159;
    struct fecha h = { 2012, 2, 29 };
    char d = '!';

    printf("var\taddress\t\tsizeof\n");
    printf("n:\t%p\t%u\n", &n, sizeof(n));
    printf("c:\t%p\t%u\n", &c, sizeof(c));
    printf("x:\t%p\t%u\n", &x, sizeof(x));
    printf("h:\t%p\t%u\n", &h, sizeof(h));
    printf("d:\t%p\t%u\n", &d, sizeof(d));

    printf("\n");
    printf("h.anno:\t%p\t%u\n", &h.anno, sizeof(h.anno));
    printf("h.mes :\t%p\t%u\n", &h.mes,  sizeof(h.mes));
    printf("h.dia :\t%p\t%u\n", &h.dia,  sizeof(h.dia));

    return 0;
}
