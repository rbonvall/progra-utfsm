Promedios de alumnos
====================

.. highlight:: c

El siguiente programa
pide al usuario ingresar las notas
de uno o más alumnos,
y va mostrando los promedios de cada uno de ellos:

.. literalinclude:: programas/promedios.c

El especificador de formato ``%.1f`` sirve para mostrar un número ``float``
con una cifra decimal.

Por ejemplo,
una ejecución del programa
podría verse así:

.. testcase::

    Ingrese nombre del alumno: `Perico`
    Cuantas notas tiene Perico? `5`
      Nota 1: `17`
      Nota 2: `26`
      Nota 3: `66`
      Nota 4: `41`
      Nota 5: `30`
    El promedio de Perico es 36.0
    Desea calcular mas promedios (si/no)? `si`
    Ingrese nombre del alumno: `Yayita`
    Cuantas notas tiene Yayita? `3`
      Nota 1: `15`
      Nota 2: `70`
      Nota 3: `91`
    El promedio de Yayita es 58.7
    Desea calcular mas promedios (si/no)? `no`

Escriba, compile y ejecute este programa.

Arreglos
--------
Un **arreglo** es una región continua en la memoria del computador
en la que se almacenan varios valores del mismo tipo.
En C se usa los arreglos como colecciones de valores,
tal como se hacía con las listas de Python.

Un arreglo llamado ``notas`` de tipo ``int`` y tamaño ``10``
se declara de la siguiente manera::

    int notas[10];

Los arreglos son mucho más limitados que las listas de Python.
Todos los elementos de un arreglo deben ser del mismo tipo.
El tamaño de un arreglo está fijo,
y debe estar especificado al momento de compilar el programa.
Por ejemplo,
es ilegal hacer lo siguiente::

    int n;
    scanf("%d", &n);

    float arreglo[n];   /* ilegal */

Por lo tanto,
lo que suele hacerse es declarar arreglos suficientemente grandes,
y llevar la cuenta de cuántos elementos han sido asignados.
Hay que tener en cuenta que,
al igual que todas las variables,
cada elemento del arreglo siempre tiene un valor,
aunque no haya sido asignado explícitamente::

    int a[5];
    a[0] = 1000;
    a[1] = 700;
    printf("%d\n", a[2]); /* Esto algo va a imprimir,
                             pero no sabemos que. */


Cada elemento está identificado a través de su índice,
que es su posición dentro del arreglo.
Los índices parten de cero:
si el arreglo tiene diez elementos,
entonces los índices van de cero a nueve.
Cada elemento del arreglo puede ser considerado
por sí solo como una variable,
a la que se accede usando el índice entre corchetes::

    int a[10];
    /* Todas las instrucciones a continuacion
       son validas. */
    a[0] = 5;
    a[1] = a[0] + 3;
    a[0]++;
    a[2] = (a[0] + a[1]) / 2.0;

Es ilegal tratar de acceder a un elemento del arreglo
cuyo índice está fuera de los límites
definidos por su tamaño.
Lamentablemente,
nunca se verifica que los índices utilizados sean válidos,
ni al momento de compilar ni durante la ejecución del programa.
Esto es una fuente de errores difíciles de detectar.
Por ejemplo,
al ejecutar este código
el programa podría seguir funcionando,
o también podría caerse estrepitosamente::

    int a[10];
    a[20] = 5;  /* ilegal */

Funciones que reciben arreglos como parámetros
----------------------------------------------
La función ``promedio`` recibe como primer parámetro
el arreglo con los valores que se van a promediar.
Lo ideal es que la función sirva para arreglos de cualquier tamaño,
no sólo para los de tamaño 10 como el del ejemplo.

En la declaración del parámetro,
hay que especificar que se trata de un arreglo,
pero no su tamaño.
Para esto, hay que poner los corchetes sin el tamaño::

    int valores[]

Sin embargo,
cada vez que se llame a la función
sí es importante conocer el tamaño del arreglo.
De otro modo,
sería imposible saber hasta qué valor promediar.
Por lo tanto,
es imprescindible pasar
el tamaño del arreglo
como parámetro adicional,
que en esta función hemos bautizado como ``cantidad``.

Note que aunque siempre estamos pasando
el mismo arreglo ``notas`` a la función,
``cantidad`` no necesariamente
tiene el mismo valor cada vez.
Esto no es importante para la función,
que operará sólo con la cantidad de valores
que se le indica.
Eso sí, la cantidad debe ser siempre
menor o igual que el tamaño verdadero del arreglo
(en este caso, 10).

Strings
-------
En C no existe un tipo de datos
para representar los strings,
como el tipo ``str`` de Python.
En C, **un string es simplemente
un arreglo de caracteres**.

Ya vimos que los arreglos deben tener un tamaño fijo.
Sin embargo,
en general uno no conoce de antemano
el largo de los textos que serán almacenado.
Esto en teoría representa un problema:
¿cómo sabe el programa cuáles de los caracteres del arreglo
son parte del texto,
y cuáles son simplemente caracteres que están allí
sólo porque el arreglo es más largo de lo que corresponde?

La manera con la que C resuelve este problema
es marcando el final del texto
con un caracter especial representado como ``'\0'``.

Por ejemplo,
después de ingresar el nombre ``Perico``,
el contenido del arreglo ``nombre``
podría ser el siguiente:

.. code-block:: none

              0   1   2   3   4   5   6   7   8  ...  19
            ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
    nombre: │ P │ e │ r │ i │ c │ o │ \0│ x │ m │...│ q │
            └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘

Lo que hay a continuación del caracter ``'\0'`` es irrelevante.
Todas las operaciones de strings
saben que el texto llega solamente hasta ahí.

Como el texto ``"Perico"`` tiene seis caracteres,
se utilizará siete casillas del arreglo
para almacenarlo.
En general,
siempre debe declararse un arreglo de caracteres
cuyo tamaño sea uno más
que el más largo de los textos que se podría almacenar.

Para leer un string como entrada
usando la función ``scanf``,
se debe usar el descriptor de formato ``%s``.
Una diferencia importante con la lectura de otros tipos de variables
es que, al leer strings,
el segundo parámetro del ``scanf`` no debe ir con el operador ``&``,
sino que debe ser la variable desnuda::

    scanf("%s", nombre);

Hay una razón técnica muy precisa para esto
que será más sencilla de comprender
una vez que sepamos más sobre la organización de la memoria,
pero por ahora aceptémoslo como un dogma:
los strings se leen sin ``&``,
valores de otros tipos con ``&``.

Todas las operaciones de strings
están implementadas como funciones
cuyas declaraciones están en la cabecera ``string.h``:

* ``strlen(s)`` retorna el largo del string ``s``,
  sin incluir el ``'\0'`` del final.
* ``strcpy(s, t)`` copia el contenido del string ``t``
  en el string ``s``;
  es necesario que el tamaño del arreglo ``s``
  sea al menor tan grande como ``t``.
* ``strcat(s, t)`` concatena el string ``t``
  al string ``s``; por ejemplo,
  al ejecutar el siguiente código,
  el string ``s`` queda con el contenido ``"Hola mundo"``::

    char s[30], t[30];
    strcpy(s, "Hola ");
    strcpy(t, "mundo");
    strcat(s, t);
    printf("%s\n", s);         /* imprime Hola mundo */
    printf("%d\n", strlen(s)); /* imprime 10 */

Ciclo do-while
--------------

El **do while** es un ciclo similar al ``while``.
El código es ejecutado mientras la condición es verdadera.
La única diferencia es que la condición del ``do while``
es evaluada al final de cada iteración,
mientras que la del ``while`` es evaluada al principio.

En otras palabras,
esto significa que el ``do while`` hace algo una o más veces,
mientras que el ``while`` lo hace cero o más veces.

En nuestro programa de ejemplo
es apropiado usar ``do while``,
ya que no tiene sentido ejecutar el programa
para no calcular ningún promedio.
Por lo tanto,
calculamos uno
y al final decidimos si queremos continuar.

La sintaxis del ciclo ``do while`` es::

    do {
        /* ... */
    }
    while (condicion);

El punto y coma al final es obligatorio.

Ejercicios
----------
¿Qué ocurre con el programa
si intenta ingresar más de una palabra
al ingresar el nombre de un alumno
(por ejemplo el nombre completo: ``Perico Los Palotes``)?
Haga la prueba.
Investigue cómo hacer para que el programa
sea capaz de leer un nombre con espacios.

¿Qué ocurre si intenta ingresar un nombre
que tenga más de 20 caracteres,
como por ejemplo ``Periiiiiiiiiiiiiiiiico``)?
Haga la prueba.


