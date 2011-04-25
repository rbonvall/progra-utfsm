Contar letras y palabras
------------------------

#. Escriba la función ``contar_letras(oracion)``
   que retorne un diccionario
   asociando a cada letra
   la cantidad de veces que aparece en la oracion::

    >>> contar_letras('El elefante avanza hacia Asia')
    {'a': 8, 'c': 1, 'e': 4, 'f': 1, 'h': 1, 'i': 2, 'l': 2, 'n': 2, 's': 1, 't': 1, 'v': 1, 'z': 1}

   Cada valor del diccionario debe considerar
   tanto las apariciones en mayúscula como en minúscula
   de la letra correspondiente.
   Los espacios deben ser ignorados.

#. Escriba la función ``contar_vocales(oracion)``
   que retorne un diccionario
   asociando a cada vocal
   la cantidad de veces que aparece en la oracion.
   Si una vocal no aparece en la oración,
   de todos modos debe estar en el diccionario
   asociada al valor 0::

    >>> contar_vocales('El elefante avanza hacia Asia')
    {'a': 8, 'e': 4, 'i': 2, 'o': 0, 'u': 0}

#. Escriba la función ``contar_iniciales(oracion)``
   que retorne un diccionario
   asociando a cada letra
   la cantidad de veces que aparece al principio de una palabra::

    >>> contar_iniciales('El elefante avanza hacia Asia')
    {'e': 2, 'h': 1, 'a': 2}
    >>> contar_iniciales('Varias vacas vuelan sobre Venezuela')
    {'s': 1', 'v': 4}

#. Escriba la función ``obtener_largo_palabras(oracion)``
   que retorne un diccionario
   asociando a cada palabra su cantidad de letras::

    >>> obtener_largo_palabras('el gato y el pato son amigos')
    {'el': 2, 'son': 3, 'gato': 4, 'y': 1, 'amigos': 6, 'pato': 4}

#. Escriba la función ``contar_palabras(oracion)``
   que retorne un diccionario
   asociando a cada palabra la cantidad de veces
   que aparece en la oración::

    >>> contar_palabras('El sobre esta sobre el pupitre')
    {'sobre': 2, 'pupitre': 1, 'el': 2, 'esta': 1}

#. Escriba la función ``palabras_repetidas(oracion)``
   que retorne una lista con las palabras que están repetidas::

    >>> palabras_repetidas('El partido termino cero a cero')
    ['cero']
    >>> palabras_repetidas('El sobre esta sobre el mueble')
    ['el', 'sobre']
    >>> palabras_repetidas('Ay, ahi no hay pan')
    []

Para obtener la lista de palabras de la oración,
puede usar el método ``split`` de los strings::

    >>> s = 'el gato y el pato'
    >>> s.split()
    ['el', 'gato', 'y', 'el', 'pato']

Para obtener un string en minúsculas,
puede usar el método ``lower``::

    >>> s = 'Venezuela'
    >>> s.lower()
    'venezuela'

