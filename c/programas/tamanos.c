#include <stdio.h>

int main() {
    printf("Tama~nos de los tipos:\n");

    /* Tipos enteros */
    printf("char:      %lu bytes\n", sizeof(char));
    printf("int:       %lu bytes\n", sizeof(int));
    printf("long int:  %lu bytes\n", sizeof(long int));
    printf("short int: %lu bytes\n", sizeof(short int));

    /* Tipos reales */
    printf("float:     %lu bytes\n", sizeof(float));
    printf("double:    %lu bytes\n", sizeof(double));

    return 0;
}
