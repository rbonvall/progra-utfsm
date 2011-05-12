Trios pitagóricos
------------------

Un trío pitagórico se define como un
conjunto de tres números, *a*, *b* y *c*
que cumplen con la relación.

.. math::

    a^{2} + b^{2} = c^{2}

Desarrolle un programa
que contenga la función
``son_pitagoricos(a, b, c)``
que retorne ``True`` si ``a``, ``b`` y ``c``
son un trío pitagórico, y ``False`` si no
lo son::

   >>> son_pitagoricos(3, 4, 5)
   True
   >>> son_pitagoricos(4, 6, 9)
   False
   >>> son_pitagoricos(5, 12, 13)
   True

A continuación, en el mismo programa escriba
la función ``pitagoricos(n)``
que retorne la lista de todos los tríos pitagóricos
(como tuplas)
todos los tríos pitagóricos cuyos valores
son menores que ``n``::

    >>> pitagoricos(18)
    [(3, 4, 5), (4, 3, 5), (5, 12, 13), (6, 8, 10), (8, 6, 10), (8, 15, 17), (9, 12, 15), (12, 5, 13), (12, 9, 15), (15, 8, 17)]

