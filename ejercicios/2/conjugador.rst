Conjugador de verbos
====================

Escriba un programa que reciba como entrada
el infinitivo de un verbo regular
y a continuación muestre su conjugación en tiempo presente:

.. testcase::

    Ingrese verbo: `amar`
    yo amo
    tu amas
    el ama
    nosotros amamos
    vosotros amais
    ellos aman

.. testcase::

    Ingrese verbo: `comer`
    yo como
    tu comes
    el come
    nosotros comemos
    vosotros comeis
    ellos comen

.. testcase::

    Ingrese verbo: `vivir`
    yo vivo
    tu vives
    el vive
    nosotros vivimos
    vosotros vivis
    ellos viven

Utilice un diccionario para asociar a cada terminación
(-ar, -er e -ir) sus declinaciones,
y una lista para guardar los pronombres en orden::

    pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

