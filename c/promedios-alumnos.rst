Promedios de alumnos
====================

.. highlight:: c

El siguiente programa
pide al usuario ingresar las notas
de uno o más alumnos,
y va mostrando los promedios de cada uno de ellos:

.. literalinclude:: programas/promedios.c

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

Strings
-------
En C no existe un tipo de datos
para representar los strings,
como el tipo ``str`` de Python.
En C, **un string es simplemente
un arreglo de caracteres**.



Por ejemplo,
después de ingresar el nombre ``Perico``,
el contenido del arreglo ``nombre``
será el siguiente:

.. code-block:: none

              0   1   2   3   4   5   6   7   8  ...  19
            +---+---+---+---+---+---+---+---+---+---+---+
    nombre: | P | e | r | i | c | o | \0|???|???|???|???|
            +---+---+---+---+---+---+---+---+---+---+---+

Como el texto ``"Perico"`` tiene seis caracteres,
se utilizará siete casillas del arreglo
para almacenarlo.

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

Ejercicio
---------
¿Qué ocurre con el programa
si intenta ingresar el nombre completo de un alumno
(por ejemplo: ``Perico Los Palotes``)?
Haga la prueba.

