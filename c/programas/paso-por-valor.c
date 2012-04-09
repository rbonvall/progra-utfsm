#include <stdio.h>

void f(int x) {
    x = 9999;
}

int main() {
    int a = 11;
    f(a);
    printf("%d\n", a);    /* imprime 11 */
    return 0;
}
