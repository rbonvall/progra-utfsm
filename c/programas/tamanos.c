#include <stdio.h>

int main() {
    printf("Tama~nos de los tipos:\n");

    /* Tipos enteros */
    printf("char:      %u bytes\n", sizeof(char));
    printf("int:       %u bytes\n", sizeof(int));
    printf("long int:  %u bytes\n", sizeof(long int));
    printf("short int: %u bytes\n", sizeof(short int));

    /* Tipos reales */
    printf("float:     %u bytes\n", sizeof(float));
    printf("double:    %u bytes\n", sizeof(double));

    return 0;
}
