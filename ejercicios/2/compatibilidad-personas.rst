Compatibilidad entre personas
-----------------------------
Para este problema,
consideraremos las siguientes características de una persona:

* nombre,
* género (masculino o femenino),
* edad,
* música favorita, y
* signo zodiacal.

En el programa a realizar,
una persona será representada como una tupla::

  persona_1 = ('Pepito', 'M', 27, 'rock', 'leo')
  persona_2 = ('Yayita', 'F', 23, 'cumbia', 'virgo')

Dos personas son compatibles
si:

* son de géneros opuestos (un hombre y una mujer),
* tienen menos de diez años de diferencia,
* les gusta la misma música, y
* sus signos zodiacales son compatibles.

Para saber los signos compatibles,
existe un conjunto ``signos_compatibles``
que tiene tuplas ``(signo_mujer, signo_hombre)``,
que `usted puede descargar aquí`_.
Si una tupla está en el conjunto,
significa que los signos son compatibles::

    >>> ('aries', 'tauro') in signos_compatibles
    True

    # Significa que mujer aries
    # es compatible con hombre tauro.

    >>> ('capricornio', 'libra') in signos_compatibles
    False

    # Significa que mujer capricornio
    # no es compatible con hombre libra.

Escriba la función ``compatibles(p1, p2)``
que indique si dos personas son compatibles o no.

.. _usted puede descargar aquí: ../../_static/signos.py

