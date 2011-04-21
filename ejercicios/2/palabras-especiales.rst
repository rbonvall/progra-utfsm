Palabras especiales
===================

#. Dos palabras son **anagramas** si tienen las mismas letras pero en otro orden.
   Por ejemplo, «torpes» y «postre» son anagramas, mientras que «aparta» y
   «raptar» no lo son, ya que «raptar» tiene una *r* de más y una *a* de menos.

   Escriba la función ``son_anagramas(p1, p2)``
   que indique si las palabras ``p1`` y ``p2`` son anagramas::

       >>> son_anagramas('torpes', 'postre')
       True
       >>> son_anagramas('aparta', 'raptar')
       False

#. Las palabras **panvocálicas** son las que tienen las cinco vocales.
   Por ejemplo: centrifugado, bisabuelo, hipotenusa.

   Escriba la función ``es_panvocalica(palabra)`` que indique
   si una palabra es panvocálica o no::

    >>> es_panvocalica('educativo')
    True
    >>> es_panvocalica('pedagogico')
    False

#. Escriba la función ``cuenta_panvocalicas(oracion)`` que cuente cuántas palabras
   panvocálicas tiene una oración::

    >>> cuenta_panvocalicas('el abuelito mordisquea el aceituno con contundencia')
    4
    >>> cuenta_panvocalicas('la contertulia estudiosa va a casa')
    2
    >>> cuenta_panvocalicas('los hipopotamos bailan al amanecer')
    0

#. Escriba la función ``tiene_letras_en_orden(palabra)``
   que indique si las letras de la palabra están en orden alfabético::

    >>> tiene_letras_en_orden('himnos')
    True
    >>> tiene_letras_en_orden('abenuz')
    True
    >>> tiene_letras_en_orden('zapato')
    False

#. Escriba la función ``tiene_letras_dos_veces(palabra)``
   que indique si cada letra de la palabra aparece exactamente dos veces::

    >>> tiene_letras_dos_veces('aristocraticos')
    True
    >>> tiene_letras_dos_veces('quisquilloso')
    True
    >>> tiene_letras_dos_veces('aristocracia')
    False

#. Escriba la función ``palabras_repetidas(oracion)``
   que entregue una lista de las palabras que están repetidas en la oración::

    >>> palabras_repetidas('El partido termino cero a cero')
    ['cero']
    >>> palabras_repetidas('El sobre esta sobre el mueble')
    ['el', 'sobre']
    >>> palabras_repetidas('Ay, ahi no hay pan')
    []

#. Un **pangrama** es un texto que tiene todas las letras del alfabeto,
   de la *a* a la *z*
   (por las limitaciones de Python 2.7, excluiremos la *ñ*).
   Escriba la función ``es_pangrama(texto)``
   que indique si el texto es o no un pangrama::

    >>> es_pangrama('Sylvia wagt quick den Jux bei Pforzheim.')
    True
    >>> es_pangrama('Cada vez que trabajo, Felix me paga un whisky.')
    True
    >>> es_pangrama('Cada vez que trabajo, Luis me invita a una cerveza.')
    False
