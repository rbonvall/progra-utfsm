Indentación
===========

Sin usar el computador,
rutee los siguientes programas
e indique cuál es la salida de los siguientes programas.

A continuación,
compruebe sus respuestas
ingresando los programas al computador.

::

    s = 0
    t = 0
    for i in range(3):
        for j in range(3):
            s = s + 1
            if i < j:
                t = t + 1
        print t
        print s

::

    s = 0
    t = 0
    for i in range(3):
        for j in range(3):
            s = s + 1
        if i < j:
            t = t + 1
            print t
    print s

::

    s = 0
    t = 0
    for i in range(3):
        for j in range(3):
            s = s + 1
    if i < j:
        t = t + 1
        print t
    print s

