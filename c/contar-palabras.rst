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
     950     Sancho
     165     Dulcinea
     894     Quijote

Contemos también cuántas veces aparecen
los artículos del idioma español en toda la obra::

    $ ./contar-palabras pg2000.txt el la los las
    7957     el
    10200    la
    4680     los
    3423     las

.. _El Quijote de la Mancha: http://www.gutenberg.org/ebooks/2000.txt.utf8

Pruebe qué ocurre al ejecutar el programa si:

* no se le entrega ningún parámetro::

    $ ./contar-palabras

* se le pasa el archivo pero ninguna palabra::

    $ ./contar-palabras pg2000.txt

* se le pasa un archivo que no existe::

    $ ./contar-palabras no-existe.txt perro gato


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
