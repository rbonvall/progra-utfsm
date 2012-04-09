#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define DELTA_THETA 0.1

int main() {
    FILE *a_trig;

    a_trig = fopen("trig.txt", "w");
    if (a_trig == NULL) {
        fprintf(stderr, "No se pudo crear el archivo trig.txt\n");
        exit(1);
    }

    fprintf(a_trig, "Angulo\tSeno\tCoseno\n");

    double theta;
    for (theta = 0.0; theta <= M_PI; theta += DELTA_THETA) {
        fprintf(a_trig, "%.2lf\t", theta);
        fprintf(a_trig, "%.4lf\t", sin(theta));
        fprintf(a_trig, "%.4lf\n", cos(theta));
    }

    fclose(a_trig);
    return 0;
}
