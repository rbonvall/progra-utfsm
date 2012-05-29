#include <stdio.h>
#include <ctype.h>

#define FOR(var)  for (var = 0; var < 8; ++var)

enum color {BLANCO, NEGRO, VACIO};

char tablero[8][8];
enum color turno;

/* Declaraciones de funciones. */
void inicializar_tablero();
void imprimir_tablero();
void mover_pieza(int, int, int, int);
int juego_terminado();
void leer_jugada(int*, int*, int*, int*);
enum color color_pieza(int, int);


int main() {
    int i_inicial, j_inicial;  /* Coordenadas de la pieza a mover. */
    int i_final,   j_final;    /* Coordenadas a donde se va a mover. */

    inicializar_tablero();
    turno = BLANCO;
    do {
        imprimir_tablero();
        leer_jugada(&i_inicial, &j_inicial, &i_final, &j_final);
        mover_pieza( i_inicial,  j_inicial,  i_final,  j_final);
        turno = 1 - turno;
    } while (!juego_terminado());

    return 0;
}


void mover_pieza(int i0, int j0, int i1, int j1) {
    tablero[i1][j1] = tablero[i0][j0];
    tablero[i0][j0] = '.';
}


void inicializar_tablero() {
    int i, j;
    char primera_fila[] = "tcadract";

    FOR (j) {
        tablero[0][j] = primera_fila[j];
        tablero[1][j] = 'p';

        for (i = 2; i < 6; ++i)
            tablero[i][j] = '.';

        tablero[6][j] = 'P';
        tablero[7][j] = toupper(primera_fila[j]);
    }
}


void imprimir_tablero() {
    int i, j;

    printf("\n   ");
    FOR (j)
        printf("%d ", j);
    printf("\n");
    printf("  +---------------+\n");

    FOR (i) {
        printf("%c |", 'a' + i);
        FOR (j)
            printf("%c ", tablero[i][j]);
        printf("\b|\n");
    }
    printf("  +---------------+\n");
}


enum color color_pieza(int i, int j) {
    if (isupper(tablero[i][j]))
        return BLANCO;
    else if (islower(tablero[i][j]))
        return NEGRO;
    else
        return VACIO;
}


void leer_jugada(int *i_inicial, int *j_inicial,
                 int *i_final,   int *j_final) {
    char desde[5], hasta[5];

    if (turno == BLANCO)
        printf("Juega blanco: ");
    else if (turno == NEGRO)
        printf("Juega negro: ");
    scanf("%s", desde);
    scanf("%s", hasta);

    *i_inicial = desde[0] - 'a';
    *j_inicial = desde[1] - '0';
    *i_final   = hasta[0] - 'a';
    *j_final   = hasta[1] - '0';
}


int juego_terminado() {
    return 0;
}

