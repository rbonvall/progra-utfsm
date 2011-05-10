Arreglos
========

*Para la materia de arreglos,
utilizaremos un módulo llamado ``numpy``,
que no viene incluido con Python.*

*Para poder usar este módulo,
usted debe descargarlo `de esta página`_
e instalarlo en su computador.*

.. _de esta página: #

Las estructuras de datos que hemos visto hasta ahora
(listas, tuplas, diccionarios, conjuntos)


En aplicaciones de Ingeniería, por otra parte,
la estructura de datos más importante
es el **arreglo**.
Un arreglo es una tabla de números
(generalmente de tipo ``float``)


Los arreglos tienen algunas similitudes con las listas:

* los elementos tienen un orden y se pueden acceder mediante su posición,
* los elementos se pueden recorrer usando un ciclo ``for``.

Sin embargo,
también tienen algunas restricciones:

* todos los elementos deben tener el mismo tipo,
* en general, el tamaño del arreglo es fijo
  (no van creciendo dinámicamente como las listas),
* se ocupan principalmente para almacenar datos numéricos.

Crear arreglos
--------------
Para usar el módulo ``numpy``,
primero debemos importarlo::

    import numpy

Si no recuerda para qué sirve el ``import``,
puede repasar la materia sobre módulos_.

.. _módulos: modulos.html

El tipo de datos de los arreglos se llama ``array``.
Para crear un arreglo nuevo,
se puede usar la función ``array``
pasándole como parámetro la lista de valores
que deseamos agregar al arreglo::

    >>> a = numpy.array([6, 1, 3, 9, 8])
    >>> a
    array([6, 1, 3, 9, 8])

Todos los elementos del arreglo
tienen exactamente el mismo tipo.
Para crear un arreglo de números reales,
basta con que uno de los valores lo sea::

    >>> b = numpy.array([6.0, 1, 3, 9, 8])
    >>> b
    array([ 6.,  1.,  3.,  9.,  8.])

Otra opción es convertir el arreglo a otro tipo
usando el método ``astype``::

    >>> a
    array([6, 1, 3, 9, 8])
    >>> a.astype(float)
    array([ 6.,  1.,  3.,  9.,  8.])
    >>> a.astype(complex)
    array([ 6.+0.j,  1.+0.j,  3.+0.j,  9.+0.j,  8.+0.j])

Hay muchas formas de arreglos
que aparecen a menudo en la práctica,
por lo que existen funciones especiales para crearlos:

* ``zeros(n)`` crea un arreglo de ``n`` ceros;
* ``ones(n)`` crea un arreglo de ``n`` unos;
* ``arange(a, b, c)`` crea un arreglo
  de forma similar a la función ``range``;
* ``linspace(a, b, n)`` crea un arreglo
  de ``n`` valores equiespaciados
  entre ``a`` y ``b``.

::

    >>> zeros(6)
    array([ 0.,  0.,  0.,  0.,  0.,  0.])
    >>> ones(5)
    array([ 1.,  1.,  1.,  1.,  1.])
    >>> arange(3.0, 9.0)
    array([ 3.,  4.,  5.,  6.,  7.,  8.])
    >>> linspace(1, 2, 5)
    array([ 1.  ,  1.25,  1.5 ,  1.75,  2.  ])

Operaciones con arreglos
------------------------
Las limitaciones que tienen los arreglos
son compensadas por la cantidad de operaciones
que permiten realizar sobre ellos.

Las operaciones aritméticas entre arreglos
se aplican elemento a elemento::

    >>> a = numpy.array([55, 21, 19, 11,  9])
    >>> b = numpy.array([12, -9,  0, 22, -9])

    # sumar los dos arreglos elemento a elemento
    >>> a + b
    array([67, 12, 19, 33,  0])

    # multiplicar
    >>> a * b
    array([ 660, -189,    0,  242,  -81])

    # restar
    >>> a - b
    array([ 43,  30,  19, -11,  18])

Las operaciones entre un arreglo y un valor simple
funcionan aplicando la operación
a todos los elementos del arreglo,
usando el valor simple como operando todas las veces::

    >>> a
    array([55, 21, 19, 11,  9])

    # multiplicar por 0.1 a todos los elementos
    >>> 0.1 * a
    array([ 5.5,  2.1,  1.9,  1.1,  0.9])

    # restar 9.0 a todos los elementos
    >>> a - 9.0
    array([ 46.,  12.,  10.,   2.,   0.])

Note que si quisiéramos hacer estas operaciones usando listas,
necesitaríamos usar un ciclo
para hacer las operaciones elemento a elemento.

