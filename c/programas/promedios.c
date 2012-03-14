#include <stdio.h>

float promedio(int valores[], int cantidad) {
    int i;
    float suma = 0.0;

    for (i = 0; i < cantidad; ++i)
        suma += valores[i];

    return suma / (float) cantidad;
}


int main() {

    int notas[10];
    char nombre[20];
    char opcion[3];
    int n, i;

    do {
        printf("Ingrese nombre del alumno: ");
        scanf("%s", nombre);

        printf("Cuantas notas tiene %s? ", nombre);
        scanf("%d", &n);

        for (i = 0; i < n; ++i) {
            printf("  Nota %d: ", i + 1);
            scanf("%d", &notas[i]);
        }

        printf("El promedio de %s es %.1f\n", nombre, promedio(notas, n));

        printf("Desea calcular mas promedios (si/no)? ");
        scanf("%s", opcion);

    } while (opcion[0] == 's' || opcion[0] == 'S');

    return 0;
}
