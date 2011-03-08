Ejercicios
==========

.. toctree::
   :maxdepth: 1

   1/index.rst
   2/index.rst
   3/index.rst

Acerca de los enunciados
------------------------

Muchos de los enunciados de los ejercicios
vienen acompañados de **casos de prueba**,
que muestran una sesión de ejemplo del programa.

En estos casos de prueba,
el texto que aparece en negrita
indica qué es lo que el usuario ingresa.
Lo que aparece en texto normal
es lo que el programa muestra.

Por ejemplo,
el siguiente es un caso de prueba de un programa:

.. testcase::

    Ingrese un numero: `2`
    El doble de 2 es 4

En este ejemplo,
el valor ``2`` en la primera línea fue ingresado por el usuario.
El resto del texto fue impreso por el programa,
ya sea usando la sentencia ``print`` o la función ``raw_input``.

Para probar su programa,
usted puede ejecutarlo e ingresar los datos
tal como se muestra en el caso de prueba,
y debe obtener la misma salida.

Si su programa pasa todos los casos de prueba exitosamente,
no significa que esté correcto,
pero por lo menos funciona para algunas entradas.

