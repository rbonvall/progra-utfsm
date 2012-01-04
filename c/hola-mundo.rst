Hola mundo
==========

.. highlight:: c

El siguiente es un programa
que le muestra al usuario
el mensaje «Hola mundo»:

.. literalinclude:: programas/hola-mundo.c
   :language: c

Escriba este programa en su entorno de desarrollo favorito.
¡No copie y pegue, escríbalo a mano!
Así se irá familiarizando con la sintaxis del lenguaje.

Compile el programa.
Si el programa no compila,
entonces cometió algún error al transcribirlo.
Lea el mensaje de error del compilador,
descubra los errores,
y arregle el programa.

Función main
------------
En un programa en C,
todas las sentencias deben estar dentro de una función.

Todos los programas deben tener una función con nombre ``main``.
El código que está dentro de la función ``main``
es lo que hace el programa cuando es ejecutado.

La línea ``int main()`` es la que indica que
el código que viene a continuación,
entre los paréntesis de llave (``{`` y ``}``)
es parte de esta función.

Cuando la función ``main`` retorna un valor,
entonces el programa se termina.
El valor que debe retornar debe ser un entero
(esto es lo que significa el ``int`` de la definición).
Si el programa se ejecuta correctamente,
entonces debe retornarse cero.
Si se retorna un valor distinto de cero,
se está indicando que ocurrió algún error
durante la ejecución del programa.

Como regla general,
al final de la función ``main``
siempre debe ir un ``return 0``, como en el ejemplo.

Salida usando printf
--------------------
La función ``printf`` muestra un mensaje en la pantalla.
El mensaje debe ser un string.
Los strings literales se representan entre comillas dobles::

    "Hola mundo\n"

A diferencia del ``print`` de Python,
``printf`` no pone un salto de línea al final del mensaje.
El salto de línea debe ser agregado explícitamente
usando su representación ``\n``.
Por ejemplo,
el siguiente código
imprime el mensaje «Hola mundo»
en una única línea,
y pone un salto de línea al final::

    printf("Ho");
    printf("la mu");
    printf("ndo\n");


Inclusión de cabeceras
----------------------
Técnicamente,
la función ``printf`` no es parte del lenguaje
(como lo es el ``print`` de Python),
sino que es parte de su `biblioteca estándar`_ de C.

La biblioteca estándar es una colección de funciones, constantes y tipos
que son utilizados comúnmente en la mayoría de los programas.
Basta con tener instalado el compilador de C
para tener toda la biblioteca estándar a disposición.

Para poder usar una función en un programa,
ella debe ser declarada en alguna parte del código.
Afortunadamente,
la biblioteca estándar provee `archivos de cabecera`_ (*header files*)
que contienen las declaraciones de todas sus funciones,
organizadas de acuerdo a su utilidad.
Los archivos de cabecera suelen tener nombres
terminados en la extensión ``.h``.

La función ``printf`` está declarada en el archivo de cabecera ``stdio.h``,
que agrupa las funciones de entrada y salida («``io``»)
de la biblioteca estándar («``std``»).
Para poder usar la función,
hay que incluir la cabecera usando la directiva ``#include``,
tal como se muestra en el ejemplo.

Más adelante veremos otros archivos de cabecera.
También podremos crear nuestras propias bibliotecas,
que requerirán sus respectivas cabeceras.

.. _biblioteca estándar: http://es.wikipedia.org/wiki/Biblioteca_est%C3%A1ndar_de_C
.. _archivos de cabecera: http://es.wikipedia.org/wiki/Archivo_de_cabecera


Ejercicio
---------
Modifique el programa
para que imprima el siguiente haiku::

    Al programar,
    cuando digo "hola mundo",
    aprendo C.

Puede hacerlo con un único ``printf``
o con varios.
