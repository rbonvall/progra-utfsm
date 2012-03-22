Contar palabras en un archivo
=============================

.. highlight:: c

El último programa que estudiaremos
cuenta cuántas veces aparecen en un archivo de texto
un conjunto de palabras indicadas por el usuario.

Copie y pegue este programa en su editor de texto
y compílelo.

.. literalinclude:: programas/contar-palabras.c

.. highlight:: console

El programa ``contar-palabras`` está diseñado
para recibir parámetros por línea de comandos.
Al momento de ejecutar el programa,
usted debe indicar inmediatamente después del nombre del programa
cuál es el archivo que quiere leer,
y cuáles son las palabras que quiere contar::

    $ ./contar-palabras archivo.txt perro gato

Para probar el programa,
descargue `El Quijote de la Mancha`_
en formato de texto plano.
El archivo se llama ``pg2000.txt``;
guárdelo en el mismo directorio
donde está el programa compilado.
Contemos cuántas veces aparecen los nombres del
Quijote, de Sancho Panza y de Dulcinea en el libro::

    $ ./contar-palabras pg2000.txt Sancho Dulcinea Quijote
       950  Sancho
       165  Dulcinea
       894  Quijote

Contemos también cuántas veces aparecen
los artículos del idioma español en toda la obra::

    $ ./contar-palabras pg2000.txt el la los las
      7957  el
     10200  la
      4680  los
      3423  las

.. _El Quijote de la Mancha: http://www.gutenberg.org/ebooks/2000.txt.utf8

Pruebe qué ocurre al ejecutar el programa si:

* no se le entrega ningún parámetro::

    $ ./contar-palabras

* se le pasa el archivo pero ninguna palabra::

    $ ./contar-palabras pg2000.txt

* se le pasa un archivo que no existe::

    $ ./contar-palabras no-existe.txt perro gato

.. highlight:: c

Lectura de archivos de texto
----------------------------
Ya aprendimos a escribir en un archivo de texto,
y ahora veremos cómo leer datos de él.

Primero que todo,
hay que abrir el archivo en modo lectura::

    FILE *f = fopen("archivo.txt", "r");

Por supuesto,
hay que verificar que ``f`` no es ``NULL``
para asegurarnos que el archivo sí pudo ser abierto.

La manera más sencilla de leer datos desde el archivo
es usar la función ``fscanf``
de la misma manera que usamos ``scanf``
para leer de la entrada estándar.
Como en nuestro programa nos interesa leer palabra por palabra,
usamos el descriptor de formato ``%s``.

Para comprobar si ya se llegó al final del archivo,
y por lo tanto ya no queda nada más que leer,
se usa la función ``feof``.
Una manera típica de leer todo el archivo
es hacerlo  como lo hicimos en nuestro programa:
un ciclo ``while`` que va verificando antes de cada lectura
si quedan o no cosas por leer::

    while (!feof(f)) {
         fscanf(f, "%s", s);

        /* ... */
    }


Arreglos son punteros, punteros son arreglos
--------------------------------------------

Parámetros del programa por línea de comandos
---------------------------------------------
Para que nuestro programa reciba parámetros
al momento de ejecutarlo,
debemos modificar la declaración de ``main``
para que incluya dos parámetros::

    int main(int argc, char **argv) {
    }

La variable ``argc`` tomará como valor
la cantidad de argumentos pasados en la línea de comandos,
*incluyendo el nombre del programa*.

El puntero ``argv`` apunta a un arreglo de ``argc`` strings,
que son precisamente estos parámetros.

(Recordemos que un string es un arreglo de ``char``,
y que un arreglo es en la práctica un puntero)
Por eso ``argv`` es un puntero a puntero a ``char``).

Por ejemplo,
cuando ejecutamos el programa de la siguiente manera:

.. code-block:: console

    $ ./contar-palabras abc.txt azul rojo verde "amarillo patito"

entonces ``argc`` tendrá el valor 6
y los valores del arreglo ``argv`` serán::

    argv[0]  →  "./contar-palabras"
    argv[1]  →  "abc.txt"
    argv[2]  →  "azul"
    argv[3]  →  "rojo"
    argv[4]  →  "verde"
    argv[5]  →  "amarillo patito"

Aritmética de punteros
----------------------

Reserva de memoria dinámica
---------------------------

Ejercicios
----------
El programa es incapaz de distinguir
cuando una palabra que está siendo buscada
aparece en mayúsculas,
o tiene pegada a ella un signo de puntuación.

Por ejemplo, para este archivo ``test.txt``:

.. code-block:: none

    Da da da? Da da da da (da da) da. Da Da!

vamos a obtener esta salida:

.. code-block:: console

    $ ./contar-palabras test.txt da
         4 da

* Modifique el programa para que
  cuente cada palabra independiente de si
  aparece con mayúsculas o minúsculas en el archivo.

* Modifique el programa para que
  cuente cada palabra incluso si aparece
  precedida o sucedida de un signo de puntuación.

