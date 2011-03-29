Módulo de listas
----------------

Desarrolle un módulo llamado ``listas.py``
que contenga las siguientes funciones.

* Una función ``promedio(l)``,
  cuyo parámetro ``l`` sea una lista de números reales,
  y que entregue el promedio de los números::

    >>> promedio([7.0, 3.1, 1.7])
    3.933333333333333
    >>> promedio([1, 4, 9, 16])
    7.5

* Una función ``cuadrados(l)``,
  que entregue una lista con los cuadrados
  de los valores de ``l``::

    >>> cuadrados([1, 2, 3, 4, 5])
    [1, 4, 9, 16, 25]
    >>> cuadrados([3.4, 1.2])
    [11.559999999999999, 1.44]

* Una función ``mas_largo(palabras)``,
  cuyo parámetro ``palabras`` es una lista de strings,
  que entregue cuál es el string más largo::

    >>> mas_largo(['raton', 'hipopotamo', 'buey', 'jirafa'])
    'hipopotamo'
    >>> mas_largo(['****', '**', '********', '**'])
    '********'

  Si las palabras más largas son varias,
  basta que entregue una de ellas.
