#include <stdio.h>

int main() {
    char c;
    int n;

    char *p = &c;
    int  *q = &n;

    printf("p:     %p    q:     %p\n", p, q);
    printf("p + 1: %p    q + 1: %p\n", p + 1, q + 1);
    printf("p + 2: %p    q + 2: %p\n", p + 2, q + 2);
    printf("p + 3: %p    q + 3: %p\n", p + 3, q + 3);
    printf("p + 4: %p    q + 4: %p\n", p + 4, q + 4);

    return 0;
}
