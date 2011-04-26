Asistencia
----------
La asistencia de los alumnos a clases puede ser llevada en una tabla como la siguiente:

 +----------+---+---+---+---+---+---+---+
 | Clase    | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
 +==========+===+===+===+===+===+===+===+
 | Pepito   | ✓ | ✓ | ✓ |   |   |   |   |
 +----------+---+---+---+---+---+---+---+
 | Yayita   | ✓ | ✓ | ✓ |   | ✓ |   | ✓ |
 +----------+---+---+---+---+---+---+---+
 | Fulanita | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
 +----------+---+---+---+---+---+---+---+
 | Panchito | ✓ | ✓ | ✓ |   | ✓ | ✓ | ✓ |
 +----------+---+---+---+---+---+---+---+

En un programa, esta informacion puede ser representada usando listas::

    >>> alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
    >>> asistencia = [
    ...  [True, True, True, False, False, False, False],
    ...  [True, True, True, False, True,  False, True ],
    ...  [True, True, True, True,  True,  True,  True ],
    ...  [True, True, True, False, True,  True,  True ]]
    >>>

#. Escriba la función ``total_por_alumno(tabla)``
   que reciba como parámetro la tabla de asistencia
   y retorne una lista con el número de clases
   a las que asistió cada alumno::

    >>> total_por_alumno(asistencia)
    [3, 5, 7, 6]

#. Escriba la función ``total_por_clase(tabla)``
   que reciba como parámetro la tabla de asistencia
   y retorne una lista con el número de alumnos
   que asistió a cada clase::

    >>> total_por_clase(asistencia)
    [4, 4, 4, 1, 3, 2, 3]

#. Escriba la función ``alumno_estrella(asistencia)``
   que indique qué alumno asistió más a clases::

    >>> alumno_estrella(asistencia)
    'Fulanita'

