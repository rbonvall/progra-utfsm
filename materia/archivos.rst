Archivos
========

.. index:: memoria RAM, almacenamiento volátil

Todos los datos que un programa utiliza durante su ejecución
se encuentran en sus variables,
que están almacenadas en la `memoria RAM`_ del computador.

La memoria RAM es un medio de almacenamiento **volátil**:
cuando el programa termina, o cuando el computador se apaga,
todos los datos se pierden para siempre.

.. index:: disco duro, almacenamiento persistente

Para que un programa pueda guardar datos de manera permanente,
es necesario utilizar un medio de almacenamiento **persistente**,
de los cuales el más importante es el `disco duro`_.

.. index:: archivo

Los datos en el disco duro están organizados en archivos_.
Un **archivo** es una secuencia de datos
almacenados en un medio persistente
que están disponibles
para ser utilizados por un programa.
Todos los archivos tienen un nombre
y una ubicación dentro del sistema de archivos del sistema operativo.

Los datos en un archivo siguen estando presentes
después de que termina el programa que lo ha creado.
Un programa puede guardar sus datos en archivos
para usarlos en una ejecución futura,
e incluso puede leer datos
desde archivos creados por otros programas.

.. _memoria RAM: http://es.wikipedia.org/wiki/Memoria_RAM
.. _disco duro: http://es.wikipedia.org/wiki/Disco_duro
.. _archivos: http://es.wikipedia.org/wiki/Archivo_(informática)

Un programa no puede manipular los datos de un archivo directamente.
Para usar un archivo, un programa siempre abrir el archivo y
asignarlo a una variable, que llamaremos el **archivo lógico**.
Todas las operaciones sobre un archivo se realizan
a través del archivo lógico.

Dependiendo del contenido,
hay muchos tipos de archivos.
Nosotros nos preocuparemos sólo de los **archivos de texto**,
que son los que contienen texto,
y pueden ser abiertos y modificados usando un editor de texto
como el Bloc de Notas.
Los archivos de texto generalmente tienen un nombre
terminado en ``.txt``.

Lectura de archivos
-------------------
Para leer datos de un archivo,
hay que abrirlo de la siguiente manera::

    archivo = open(nombre)

``nombre`` es un string que tiene el nombre del archivo.
``archivo`` es el archivo lógico a través del que
se manipulará el archivo.

Si el archivo no existe,
ocurrirá un **error de entrada y salida** (``IOError``).

La manera más simple de leer el contenido de un archivo
es hacerlo línea por línea.
Para esto, basta con poner el archivo lógico en un ciclo for::

    for linea in archivo:
        # hacer algo

Una vez que los datos han sido leídos del archivo,
hay que cerrarlo::

    archivo.close()

Por ejemplo,
supongamos que tenemos el archivo ``himno.txt``
que tiene el siguiente contenido:

.. code-block:: none

    Puro Chile
    es tu cielo azulado
    puras brisas
    te cruzan también.

El archivo tiene cuatro líneas.
Cada línea termina con un salto de línea (``\n``),
que indica que a continuación comienza una línea nueva.

El siguiente programa imprime
la primera letra de cada línea del himno::

    archivo = open('himno.txt')
    for linea in archivo:
        print linea[0]
    archivo.close()

El ciclo for es ejecutado cuatro veces,
una por cada línea del archivo.
La salida del programa es:

.. testcase::

    P
    e
    p
    t

Otro ejemplo:
el siguiente programa
imprime cuántos símbolos hay en cada línea::

    archivo = open('himno.txt')
    for linea in archivo:
        print len(linea)
    archivo.close()

La salida es:

.. testcase::

    11
    20
    13
    19

Note que el salto de línea (el "enter")
es considerado en la cuenta:

.. code-block:: none

    +---+---+---+---+---+---+---+---+---+---+---+
    | P | u | r | o |   | C | h | i | l | e | \n| = 11 símbolos
    +---+---+---+---+---+---+---+---+---+---+---+

Para obtener el string sin el salto de línea,
se puede usar el método ``strip``,
que elimina todos los símbolos de espaciado
al principio y al final del string::

    >>> s = '   Hola\n'
    >>> s.strip()
    'Hola'

Si modificamos el programa
para eliminar el salto de línea::

    archivo = open('himno.txt')
    for linea in archivo:
        print len(linea.strip())
    archivo.close()

entonces la salida es:

.. testcase::

    10
    19
    12
    18

Lo importante es comprender
que los archivos son leídos línea por línea
usando el ciclo ``for``.

Escritura en archivos
---------------------
Los ejemplos anteriores suponen que el archivo por leer existe,
y está listo para ser abierto y leído.
Ahora veremos cómo crear los archivos y cómo escribir datos en ellos,
para que otro programa después pueda abrirlos y leerlos.

Uno puede crear un archivo vacío
abriéndolo de la siguiente manera::

    archivo = open(nombre, 'w')

El segundo parámetro de la función ``open``
indica el uso que se le dará al archivo.
``'w'`` significa «escribir» (*write* en inglés).

Si el archivo señalado no existe, entonces será creado.
Si ya existe, entonces será sobreescrito.
Hay que tener cuidado entonces,
pues esta operación elimina los datos del archivo que existía previamente.

Una vez abierto el archivo,
uno puede escribir datos en él
usando el método ``write``::

    a = open('prueba.txt', 'w')
    a.write('Hola ')
    a.write('mundo.')
    a.close()

Una vez ejecutado este programa,
el archivo ``prueba.txt`` será creado
(o sobreescrito, si ya existía).
Al abrirlo en el Bloc de Notas,
veremos este contenido::

    Hola mundo.

Para escribir varias líneas en el archivo,
es necesario agregar explícitamente los saltos de línea
en cada string que sea escrito.
Por ejemplo,
para crear el archivo ``himno.txt`` que usamos más arriba,
podemos hacerlo así::

    a = open('himno.txt', 'w')
    a.write('Puro Chile\n')
    a.write('es tu cielo azulado\n')
    a.write('puras brisas\n')
    a.write('te cruzan también.\n')
    a.close()

Además del modo ``'w'`` (*write*), también existe el modo ``'a'`` (*append*),
que permite escribir datos al final de un archivo existente.
Por ejemplo, el siguiente programa abre el archivo ``prueba.txt``
que creamos más arriba, y agrega más texto al final de él::

    a = open('prueba.txt', 'a')
    a.write('\n')
    a.write('Chao ')
    a.write('pescao.')
    a.close()

Si abrimos el archivo ``prueba.txt`` en el Bloc de Notas,
veremos esto::

    Hola mundo.

    Chao pescao.

De haber abierto el archivo en modo ``'w'`` en vez de ``'a'``,
el contenido anterior (la frase ``Hola mundo``)
se habría borrado.

.. Archivos de valores separados
.. -----------------------------
.. Una manera de usar archivos
.. es para almacenar una secuencia de filas
.. compuestas por varios datos.
.. A esto se le llama **archivo de registros**,
.. y es similar a guardar una tabla de datos.
.. 
.. La manera de hacerlo es
.. asociando cada fila de la tabla a una línea del archivo,
.. y usando un símbolo delimitador para separar los datos.
.. 
.. Por ejemplo,
.. supongamos que queremos guardar en un archivo
.. los datos de esta tabla:
.. 
..     =========== =========== ======= ======= ======= =======
..     Nombre      Apellido    Nota 1  Nota 2  Nota 3  Nota 4
..     ----------- ----------- ------- ------- ------- -------
..     Perico      Los Palotes 2,1     3,4     5,5     6,4
..     Yayita      Vinagre     4,0     4,0     4,1     3,7
..     Marcelo     Bielsa      6,1     6,7     7,0     3,0
..     ...         ...         ...     ...     ...     ...
..     =========== =========== ======= ======= ======= =======
.. 
.. Si usamos el símbolo ``:`` como delimitador,
.. el archivo, que llamaremos ``alumnos.txt`` queda así::
.. 
..     Perico:Los Palotes:2.1:3.4:5.5:6.4
..     Yayita:Vinagre:4.0:4.0:4.1:3.7
..     Marcelo:Bielsa:6.1:6.7:7.0:3.0
.. 
.. Para leer los datos del archivo,
.. hay que hacerlo línea por línea,
.. tal como lo hacíamos antes.
.. Al leer cada línea, obtenemos un string.
.. Por ejemplo,
.. al leer la primera línea,
.. lo que tenemos es::
.. 
..     'Perico:Los Palotes:2.1:3.4:5.5:6.4\n'
.. 
.. Para poder usar los datos,
.. hay que descomponer los elementos del string
.. (usando ``.strip(delimitador)``)
.. y convertirlos al tipo apropiado.
.. La manera de leer el archivo ``alumnos.txt``
.. es la siguiente::
.. 
..     archivo_alumnos = open('alumnos.txt')
..     for linea in archivo_alumnos:
..         linea = linea.strip()
..         l = linea.split(':')
..         nombre = l[0]
..         apellido = l[1]
..         nota1 = float(l[2])
..         nota2 = float(l[3])
..         nota3 = float(l[4])
..         nota4 = float(l[5])
.. 
..         # hacer algo con los datos
.. 
..     archivo_alumnos.close()
.. 
.. Es lo mismo que hacíamos antes,
.. pero con un poco más de burocracia:
.. antes de usar los datos,
.. hay que extraerlos de la línea leída,
.. que es un string.
.. 
.. Una manera más corta de hacer lo mismo
.. es ésta::
.. 
..     archivo_alumnos = open('alumnos.txt')
..     for linea in archivo_alumnos:
..         l = linea.strip().split(':')
..         nombre, apellido = l[0:2]
..         n1, n2, n3, n4 = map(float, l[2:6])
.. 
..         # hacer algo
.. 
..     archivo_alumnos.close()
.. 
.. (Recordar que ``l[i:j]`` es una rebanada de la lista ``l``
.. desde el elemento ``i`` hasta el ``j``, sin incluir el último,
.. y que ``map(f, lst)`` aplica la función ``f``
.. a cada elemento de la lista ``lst``).
.. 
.. Por ejemplo,
.. si queremos imprimir el promedio de cada alumno,
.. se hace así::
.. 
..     archivo_alumnos = open('alumnos.txt')
..     for linea in archivo_alumnos:
..         l = linea.strip().split(':')
..         nombre, apellido = l[0:2]
..         n1, n2, n3, n4 = map(float, l[2:6])
..         promedio = (n1 + n2 + n3 + n4) / 4
..         print(nombre, 'obtuvo promedio', promedio)
..     archivo_alumnos.close()
.. 
.. Si queremos escribir los datos en un archivo de registro,
.. hay que crear manualmente la línea,
.. convirtiendo los datos a strings
.. y pegándolos con el delimitador.
.. 
.. Por ejemplo,
.. si queremos leer los datos del archivo de alumnos,
.. y crear un nuevo archivo ``promedios.txt``
.. que tenga sólo los promedios,
.. habría que hacerlo de la siguiente manera::
.. 
..     archivo_alumnos = open('alumnos.txt')
..     archivo_promedios = open('promedios.txt', 'w')
..     for linea in archivo_alumnos:
..         # extraer los datos
..         l = linea.strip().split(':')
..         nombre, apellido = l[0:2]
..         n1, n2, n3, n4 = map(float, l[2:6])
.. 
..         # calcular el promedio
..         promedio = (n1 + n2 + n3 + n4) / 4
.. 
..         # crear la línea para escribirla
..         # en el archivo de promedios
..         linea = nombre + ':' + apellido + ':' + str(promedio)
.. 
..         # escribir la línea en el nuevo archivo
..         print(linea, file=archivo_promedios)
.. 
..     archivo_alumnos.close()
..     archivo_promedios.close()
.. 
.. Tarea
.. ~~~~~
.. Para cada alumno en el archivo ``alumnos.txt``,
.. crear un archivo llamado ``nombre-apellido.txt``
.. que sea una carta para el alumno
.. con el siguiente contenido:
.. 
.. .. code-block:: none
.. 
..     Estimado [nombre],
..     usted ha [aprobado/reprobado]
..     con promedio [p].
.. 
.. Por ejemplo,
.. la carta para Marcelo Bielsa
.. se llamará ``marcelo-bielsa.txt``
.. y su contenido será:
.. 
.. .. code-block:: none
.. 
..     Estimado Marcelo,
..     usted ha aprobado
..     con promedio 5.7.
.. 
.. .. include:: disqus.rst
.. 
