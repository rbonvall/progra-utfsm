Recorrido de diccionarios
-------------------------
**Ejercicio 1:**
escriba una función ``hay_llaves_pares(d)``
que indique si el diccionario ``d`` tiene alguna llave
que sea un número par.

A continuación, escriba una función ``hay_valores_pares(d)``
que indique si el diccionario ``d`` tiene algún valor
que sea un número par.

Para probar las funciones, ocupe diccionarios
cuyas llaves y valores sean sólo números enteros::

    >>> d1 = {1: 2, 3: 5}
    >>> d2 = {2: 1, 6: 7}
    >>> hay_valores_pares(d1)
    True
    >>> hay_valores_pares(d2)
    False
    >>> hay_llaves_pares(d1)
    False
    >>> hay_llaves_pares(d2)
    True

**Ejercicio 2:**
escriba una función ``maximo_par(d)``
que entregue el valor máximo
de la suma de una llave y un valor
del diccionario ``d``::

    >>> d = {5: 1, 4: 7, 9: 0, 2: 2}
    >>> maximo_par(d)
    11

**Ejercicio 3:**
escriba una función ``invertir(d)``
que entregue un diccionario
cuyas llaves sean los valores de ``d``
y cuyos valores sean las llaves respectivas::

    >>> invertir({1: 2, 3: 4, 5: 6})
    {2: 1, 4: 3, 6: 5}
    >>> apodos = {
    ...   'Suazo': 'Chupete',
    ...   'Sanchez': 'Maravilla',
    ...   'Medel': 'Pitbull',
    ...   'Valdivia': 'Mago',
    ... }
    >>> invertir(apodos)
    {'Maravilla': 'Sanchez', 'Mago': 'Valdivia', 'Chupete': 'Suazo', 'Pitbull': 'Medel'}


