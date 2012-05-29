#include <stdio.h>

int main() {
    int a;
    int b;
    int *c;

    a = 2;
    b = 3;

    printf("a: %d, b: %d\n", a, b);

    c = &a;
    *c = 5;

    printf("a: %d, b: %d\n", a, b);

    c = &b;
    *c = 6;

    printf("a: %d, b: %d\n", a, b);

    printf("*c: %d\n", *c);
    b = 8;
    printf("*c: %d\n", *c);

    return 0;
}
