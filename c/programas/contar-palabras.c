#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LARGO_PALABRA 50

int main(int argc, char **argv) {
    int n;
    char **palabras;
    int *cuentas;
    FILE *f;
    char palabra_actual[MAX_LARGO_PALABRA];
    int i;

    if (argc < 3) {
        fprintf(stderr, "Uso: %s ARCHIVO PALABRA1 PALABRA2 ...\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    n = argc - 2;
    palabras = argv + 2;

    cuentas = malloc(argc * sizeof(int));
    if (cuentas == NULL) {
        fprintf(stderr, "Memoria insuficiente para ejecutar el programa.\n");
        exit(EXIT_FAILURE);
    }

    f = fopen(argv[1], "r");
    if (f == NULL) {
        fprintf(stderr, "No se pudo abrir el archivo %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    for (i = 0; i < n; ++i) {
        cuentas[i] = 0;
    }

    while (!feof(f)) {
        fscanf(f, "%s", palabra_actual);
        for (i = 0; i < n; ++i) {
            if (strcmp(palabra_actual, palabras[i]) == 0) {
                cuentas[i]++;
            }
        }
    }

    for (i = 0; i < n; ++i) {
        printf("%6d\t %s\n", cuentas[i], palabras[i]);
    }

    fclose(f);
    free(cuentas);
    exit(EXIT_SUCCESS);
}

