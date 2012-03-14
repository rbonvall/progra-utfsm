#include <stdio.h>
#include <stdlib.h>

#define ANNO_ACTUAL 2012
#define LARGO_NOMBRE 50
#define LARGO_RUT 10

struct fecha {
    int dia;
    int mes;
    int anno;
};

struct persona {
    char nombre[LARGO_NOMBRE + 1];
    char rut[LARGO_RUT + 1];
    struct fecha fecha_nacimiento;
};


int fecha_es_valida(struct fecha f) {
    int dias_mes[] = {0, 31, 28, 31, 30,
                         31, 30, 31, 31,
                         30, 31, 30, 31};

    if (f.mes < 1 || f.mes > 12)
        return 0;
    if (f.dia < 1 || f.dia > dias_mes[f.mes])
        return 0;
    return 1;
}


int main() {

    struct persona p;

    printf("Nombre completo: ");
    scanf("%[^\n]", p.nombre);

    printf("Rut: ");
    scanf("%s", p.rut);

    printf("Fecha de nacimiento (dia mes anno): ");
    scanf("%d", &p.fecha_nacimiento.dia);
    scanf("%d", &p.fecha_nacimiento.mes);
    scanf("%d", &p.fecha_nacimiento.anno);

    if (!fecha_es_valida(p.fecha_nacimiento)) {
        fprintf(stderr, "Fecha es invalida\n");
        exit(1);
    }

    printf("\n");
    printf("%s tiene %d annos.\n",
            p.nombre, ANNO_ACTUAL - p.fecha_nacimiento.anno);

    exit(0);
}

