Diccionarios
============
.. index:: diccionario

Un **diccionario** es un tipo de datos
que sirve para asociar pares de objetos.

.. index:: llave (diccionario), valor (diccionario)

Un diccionario puede ser visto
como una colección de **llaves**,
cada una de las cuales tiene asociada un **valor**.
Las llaves no están ordenadas
y no hay llaves repetidas.
La única manera de acceder a un valor
es a través de su llave.

Cómo crear diccionarios
-----------------------
Los diccionarios literales se crean usando llaves (``{`` y ``}``).
La llave y el valor van separados por dos puntos::

    >>> telefonos = {'Pepito': 5552437, 'Jaimito': 5551428, 'Yayita': 5550012}

En este ejemplo,
las llaves son ``'Pepito'``, ``'Jaimito'`` y ``'Yayita'``,
y los valores asociados a ellas son, respectivamente,
``5552437``, ``5551428`` y ``5550012``.

Un diccionario vacío puede ser creado usando ``{}`` o con la función ``dict()``::

    >>> d = {}
    >>> d = dict()

Cómo usar un diccionario
------------------------
El valor asociado a la llave ``k`` en el diccionario ``d``
se puede obtener mediante ``d[k]``::

    >>> telefonos['Pepito']
    5552437
    >>> telefonos['Jaimito']
    5551428

A diferencia de los índices de las listas,
las llaves de los diccionarios no necesitan ser números enteros.

Si la llave no está presente en el diccionario,
ocurre un **error de llave** (``KeyError``)::

    >>> telefonos['Fulanito']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'Fulanito'

Se puede agregar una llave nueva
simplemente asignándole un valor::

    >>> telefonos['Susanita'] = 4448139
    >>> telefonos
    {'Pepito': 5552437, 'Susanita': 4448139, 'Jaimito': 5551428, 'Yayita': 5550012}

Note que el orden en que quedan las llaves en el diccionario
no es necesariamente el mismo orden en que fueron agregadas.

Si se asigna un valor a una llave que ya estaba en el diccionario,
el valor anterior se sobreescribe.
Recuerde que un diccionario no puede tener llaves repetidas::

    >>> telefonos
    {'Pepito': 5552437, 'Susanita': 4448139, 'Jaimito': 5551428, 'Yayita': 5550012}
    >>> telefonos['Jaimito'] = 4448139
    >>> telefonos
    {'Pepito': 5552437, 'Susanita': 4448139, 'Jaimito': 4448139, 'Yayita': 5550012}

Los valores sí pueden estar repetidos.
En el ejemplo anterior, Jaimito y Susanita tienen el mismo número.

Para borrar una llave, se puede usar la sentencia ``del``::

    >>> del telefonos['Yayita']
    >>> telefonos
    {'Pepito': 5552437, 'Susanita': 4448139, 'Jaimito': 4448139}

Los diccionarios son iterables.
Al iterar sobre un diccionario en un ciclo ``for``,
se obtiene las llaves::

    >>> for k in telefonos:
    ...     print k
    ...
    Pepito
    Susanita
    Jaimito

Para iterar sobre las llaves, se usa ``d.values()``::

    >>> for v in telefonos.values():
    ...     print v
    ...
    5552437
    4448139
    4448139

Para iterar sobre las llaves y los valores simultáneamente,
se usa el método ``d.items()``::

    >>> for k, v in telefonos.items():
    ...     print 'El telefono de', k, 'es', v
    ...
    El telefono de Pepito es 5552437
    El telefono de Susanita es 4448139
    El telefono de Jaimito es 4448139


También es posible crear listas de llaves o valores::

    >>> list(telefonos)
    ['Pepito', 'Susanita', 'Jaimito']
    >>> list(telefonos.values())
    [5552437, 4448139, 4448139]

``len(d)`` entrega cuántos pares llave-valor hay en el diccionario::

    >>> numeros = {15: 'quince', 24: 'veinticuatro'}
    >>> len(numeros)
    2
    >>> len({})
    0

``k in d`` permite saber si la llave ``k`` está en el diccionario ``d``::

    >>> patas = {'gato': 4, 'humano': 2, 'pulpo': 8, 'perro': 4, 'ciempies': 100}
    >>> 'perro' in patas
    True
    >>> 'gusano' in patas
    False

Para saber si una llave *no* está en el diccionario,
se usa el operador ``not in``::

    >>> 'gusano' not in patas
    True


Restricciones sobre las llaves
------------------------------
No se puede usar cualquier objeto como llave de un diccionario.
Las llaves deben ser de un tipo de datos inmutable.
Por ejemplo, no se puede usar listas::

    >>> d = {[1, 2, 3]: 'hola'}
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    TypeError: unhashable type: 'list'

Típicamente, se usa números, tuplas y strings como llaves de los diccionarios.

