#include <stdio.h>

int main(void) {
    int nacimiento;
    int actual;
    int edad;

    printf("Ingrese su anno de nacimiento: ");
    scanf("%d", &nacimiento);

    printf("Ingrese el anno actual: ");
    scanf("%d", &actual);

    edad = actual - nacimiento;
    printf("Usted tiene %d annos de edad\n", edad);

    return 0;
}

