Compilación de programas en la consola
======================================






Los sistemas operativos tipo Unix,
como Linux o Mac OS,
vienen de fábrica con entornos de consola.
En Mac la consola del sistema se llama Terminal.
En Linux tiene varios para escoger:
Gnome Terminal, Konsole o XTerm, entre otros.

En Windows usted puede instalar un entorno tipo Unix
(por ejemplo Cygwin)
para disponer de una consola funcional
para probar los siguientes ejemplos.

En los ejemplos de sesiones de consola
que se muestran a continuación,
el signo ``$`` representa al **prompt**,
que es lo que sea que aparezca en su terminal
para indicarle que ya puede ingresar una instrucción.
El signo ``$`` no es parte del comando,
y no debe ser escrito en el teclado.

Las líneas que no comienzan con ``$``
muestran la salida del último comando ejecutado.

Algunos comandos útiles
para manejarse en la consola:

* ``mkdir`` crea un directorio nuevo,
* ``cd`` sirve para cambiar el directorio actual,
* ``pwd`` muestra el directorio actual,
* ``ls`` muestra los archivos en el directorio actual.

.. code-block:: console

    $ mkdir programacion
    $ ls
    programacion
    $ cd programacion
    $ pwd
    /home/usuario/programacion
    $


Compilación usando gcc
----------------------
Gcc es el más popular de los compiladores de C.
Gcc es libre y multiplataforma,
lo que asegura que puede instalarlo y usarlo
casi en cualquier sistema,
y sin necesidad de pagar una licencia.

Para compilar un programa llamado ``test.c``
que está en el mismo directorio donde estamos parados,
hay que hacerlo así:

.. code-block:: console

    $ gcc test.c -o test

Esta instrucción indica a gcc
que debe compilar el archivo fuente ``test.c``,
y crear un binario ejecutable llamado ``test``.

La opción ``-o`` señala que lo que viene a continuación
es el nombre del archivo de salida (*output*)
que debe ser creado por el compilador.
Si usted omite esta opción,
entonces el ejecutable será creado con el nombre ``a.out``:

.. code-block:: console

    $ ls
    test.c
    $ gcc test.c
    $ ls
    a.out  test.c

No sea flojo:
siempre especifique el nombre del archivo de salida.

Compilación usando make
-----------------------
Make es un programa muy útil que sí nos permite ser flojos.
Make conoce las maneras más comunes
de compilar programas en C (y en otros lenguajes también),
y hace el trabajo por nosotros.

Para programas pequeños como los que haremos aquí
no es mucho lo que ayuda,
pero conviene aprender a usarlo
porque es muy utilizado para automatizar la compilación
de proyectos más grandes.

Al ejecutar make,
no se debe indicar cómo compilar,
sino lo que uno quiere obtener.
En nuestro caso,
es el ejecutable ``test``:

.. code-block:: console

    $ ls
    test.c
    $ make test
    cc     test.c   -o test
    $ ls
    test  test.c
    $

Make sabe que si queremos obtener un binario llamado ``test``,
y en el directorio hay un archivo fuente llamado ``test.c``,
lo que hay que hacer es invocar al compilador de C.

Por omisión,
make usa el compilador ``cc``
cuando le toca compilar un archivo ``.c``.
De todos modos,
lo más probable es que en su sistema
``cc`` sea un enlace simbólico a ``gcc``:

.. code-block:: console

    $ which cc
    /usr/bin/cc
    $ ls -o /usr/bin/cc
    lrwxrwxrwx. 1 root 3 ene  5 22:01 /usr/bin/cc -> gcc
    $

Para indicar explícitamente a make
que utilice el compilador gcc (o cualquier otro) para compilar,
se debe asignar el nombre del compilador
a la variable de entorno ``CC``
usando la instrucción ``export``:

.. code-block:: console

    $ make test
    cc     test.c   -o test
    $ rm test
    $ export CC=gcc
    $ make test
    gcc     test.c   -o test
    $

Una de las gracias de make
es que sólo hace la compilación
si es que el archivo con el código
ha sido modificado desde la última vez que se compiló.
Si no ha habido cambios desde entonces,
make no hace nada:

.. code-block:: console

    $ ls
    test.c
    $ make test
    cc     test.c   -o test
    $ make test
    make: `test' está actualizado.
    $

