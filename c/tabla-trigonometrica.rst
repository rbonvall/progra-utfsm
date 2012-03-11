Escribir tabla trigonométrica
=============================

.. highlight:: c

El siguiente programa
crea un archivo llamado ``trig.txt``
que contiene una tabla
con los senos y los cosenos
de números reales entre 0 y π,
de 0.1 en 0.1.

.. literalinclude:: programas/trig.c

Si intenta compilar este programa
tal como viene haciéndolo hasta ahora,
es probable que el compilador arroje un error
parecido a «referencia indefinida a sin».
Para evitar este error,
debe agregar la opción ``-lm`` al momento de compilar
---ya explicaremos por qué---:

.. code-block:: console

    $ gcc trig.c -lm -o trig

Transcriba, compile y ejecute el programa.
Verá que un archivo llamado ``trig.txt``
fue creado.
Vea el contenido de ese archivo.
Si está trabajando en la consola,
puede usar la instrucción ``cat``:

.. code-block:: console

    $ cat trig.txt

Escritura de archivos
---------------------


Tipos de datos de coma flotante
-------------------------------
En nuestro programa decidimos declarar la variable ``theta`` como ``double``,
que es otro tipo de datos asociado a los números reales.

Los números reales no pueden ser representados exactamente en un computador,
sino que deben ser aproximados de alguna manera que sea
lo suficientemente general como para abarcar a la vez
valores muy grandes y muy pequeños,
como los que suelen aparecer en ciencia e ingeniería.

La manera estándar que utilizan los computadores para esto
es la `representación de coma flotante`_,
que es una especie de notación científica en base 2.

El tipo ``float`` que habíamos usado hasta ahora
utiliza 32 bits para representar números reales.
Lo podemos verificar al imprimir el valor de ``sizeof(float)``.
De estos 32 bits,
1 es para almacenar el signo del número,
8 son para almacenar el exponente de la base,
y el resto son para el factor que la acompaña (llamado *mantisa*).
Esto permite al tipo ``float`` representar números reales
con aproximadamente 7 cifras decimales de precisión.

A veces esta precisión no es suficiente,
y para ello existe el tipo ``double``,
que dedica 64 bits para representar el número.
Esto permite alcanzar una precisión de aproximadamente 15 cifras decimales.

A pesar de lo que parecen indicar sus nombres,
ambos tipos son representaciones de coma flotante.
A los valores ``float`` se le llama «de precisión simple»
y a los ``double``, bueno, «de precisión doble».

.. _representación de coma flotante: http://es.wikipedia.org/wiki/Coma_flotante

Biblioteca matemática
---------------------
La biblioteca estándar de C provee la cabecera ``math.h``
con funciones y constantes matemáticas.


Descriptores de formato para números reales
-------------------------------------------

Enlazado de bibliotecas
-----------------------
¿Por qué hubo que agregar el ``-lm`` al compilar?

En general, al usar bibliotecas,
no basta con sólo incluir al archivo de cabecera,
sino que además es necesario indicar al compilador
que debe enlazar nuestro programa compilado
con la biblioteca.

La razón es que la cabecera contiene sólo las declaraciones,
pero no las implementaciones de las funciones,
que están en algún archivo ya compilado
que se encuentra instalado en alguna parte de nuestro sistema.

Las funciones de la mayoría de las cabeceras estándares
están implementadas en una biblioteca llamada ``libc``.
que es enlazada automáticamente al compilar cualquier programa.

Por `razones históricas`_ que podemos obviar,
las funciones matemáticas no están implementadas en ``libc``
sino en otra biblioteca llamada ``libm``,
que no es enlazada automáticamente.

Para enlazar ``libm`` al momento de compilar
es que se agrega la opción ``-lm``.
Si quisiera enlazar explícitamente con ``libc``,
podría agregar ``-lc``, pero esto no tendría ningún efecto.

Cuando usted, más adelante, sea ya una experta programadora en C
y comience a usar bibliotecas escritas por otros desarrolladores
(o incluso por usted misma),
deberá siempre tener el cuidado de enlazarlas correctamente
al momento de compilar usando la opción ``-lnombre_de_la_biblioteca``.

.. _razones históricas: http://stackoverflow.com/questions/1033898/why-do-you-have-to-link-the-math-library-in-c

Ejercicios
----------
Interprete qué es lo que ocurre
al usar los siguientes descriptores de formato
para imprimir los valores en el archivo:

* ``"%.2lf``
* ``"% .2lf``
* ``"%+.2lf``
* ``"%lf``
* ``"%lg``

Modifique el programa
para que escriba una columna adicional
con el logaritmo natural
de cada número.

