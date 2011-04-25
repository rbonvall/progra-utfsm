Acordes
=======
En teoría musical,
la escala cromática está formada por doce notas::

    notas = ['do', 'do#', 're', 're#', 'mi', 'fa',
             'fa#', 'sol', 'sol#', 'la', 'la#', 'si']

El signo ♯ se lee «sostenido».

Cada nota corresponde a una tecla del piano.
Los sostenidos son las teclas negras:

  .. image:: ../../diagramas/piano.png

La escala es circular, y se extiende infinitamente en ambas direcciones.
Esto signfica que después de si viene nuevamente do.

Cada par de notas consecutivas está separada por un semitono.
Por ejemplo, entre re y sol♯ hay 6 semitonos.

Un acorde_ es una combinación de notas que suenan bien al unísono.

.. _acorde: http://es.wikipedia.org/wiki/Acorde

Existen varios tipos de acordes,
que difieren en la cantidad de semitonos
por las que sus notas están separadas.

Por ejemplo,
los acordes mayores tienen tres notas
separadas por 4 y 3 semitonos.
Así es como el acorde de re mayor está formado por las notas:

    re, fa♯ y la,

pues entre re y fa♯ hay 4 semitonos,
y entre fa♯ y la, 3.

Algunos tipos de acordes
están presentados en el siguiente diccionario,
asociados a las separaciones entre notas consecutivas del acorde::

    acordes = {
        'mayor': (4, 3),
        'menor': (3, 4),
        'aumentado': (4, 4),
        'disminuido': (3, 3),
        'sus 2': (2, 5),
        'sus 4': (5, 2),
        '5': (7,),
        'menor 7': (3, 4, 3),
        'mayor 7': (4, 3, 4),
        '7': (4, 3, 3),
    }

Escriba la función  ``acorde(nota, tipo)``
que entegue una lista de las notas del acorde en el orden correcto::

    >>> acorde('la', 'mayor')
    ['la', 'do#', 'mi']
    >>> acorde('sol#', 'menor')
    ['sol#', 'si', 'do#']
    >>> acorde('si', '7')
    ['si', 're#', 'fa#', 'la']
    >>> acorde('do#', '5')
    ['do#', 'sol#']

Si el tipo no es entregado,
la función debe suponer que el acorde es mayor::

    >>> acorde('si')
    ['si', 're#', 'fa#']

