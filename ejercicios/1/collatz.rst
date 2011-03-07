Secuencia de Collatz
====================

La secuencia de Collatz de un número entero
se construye de la siguiente forma:

* si el número es par, se lo divide por dos;
* si es impar, se le multiplica tres y se le suma uno;
* la sucesión termina al llegar a uno.

La `conjetura de Collatz`_ afirma que, al partir desde cualquier número,
la secuencia siempre llegará a 1.
A pesar de ser una afirmación a simple vista muy simple,
no se ha podido demostrar si es cierta o no.

.. _conjetura de Collatz: http://es.wikipedia.org/wiki/Conjetura_de_Collatz

Usando computadores, se ha verificado que la sucesión efectivamente llega a 1
partiendo desde cualquier número natural menor que `2^{58}`.

#. Desarrolle un programa
   que entregue la secuencia de Collatz de un número entero:

   .. testcase::

        n: `18`
        18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

   .. testcase::

        n: `19`
        19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

   .. testcase::

        n: `20`
        20 10 5 16 8 4 2 1

#. Desarrolle un programa
   que grafique los largos de las secuencias de Collatz
   de los números enteros positivos
   menores que el ingresado por el usuario:

   .. testcase::

        n: `20`
        1 *
        2 **
        3 ********
        4 ***
        5 ******
        6 *********
        7 *****************
        8 ****
        9 ********************
        10 *******
        11 ***************
        12 **********
        13 **********
        14 ******************
        15 ******************
        16 *****
        17 *************
        18 *********************
        19 *********************
        20 ********

