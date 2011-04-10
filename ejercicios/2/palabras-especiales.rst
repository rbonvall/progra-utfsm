Palabras especiales
===================

#. Dos palabras son **anagramas** si tienen las mismas letras pero en otro orden.
   Por ejemplo, «torpes» y «postre» son anagramas, mientras que «aparta» y
   «raptar» no lo son, ya que «raptar» tiene una *r* de más y una *a* de menos.
   
   Escriba una función ``son_anagramas(p1, p2)``,
   que indique si las palabras ``p1`` y ``p2`` son anagramas::
   
       >>> son_anagramas('torpes', 'postre')
       True
       >>> son_anagramas('aparta', 'raptar')
       False

#. Las palabras **panvocálicas** son las que tienen las cinco vocales.
   Por ejemplo: centrifugado, bisabuelo, hipotenusa.

   Escriba una función ``es_panvocalica(palabra)`` que indique
   si una palabra es panvocálica o no::

    >>> es_panvocalica('educativo')
    True
    >>> es_panvocalica('pedagogico')
    False

#. Escriba una función ``cuenta_panvocalicas(oracion)`` que cuente cuántas palabras
   panvocálicas tiene una oración::

    >>> cuenta_panvocalicas('el abuelito mordisquea el aceituno con contundencia')
    4
    >>> cuenta_panvocalicas('la contertulia estudiosa va a casa')
    2
    >>> cuenta_panvocalicas('los hipopotamos bailan al amanecer')
    0

