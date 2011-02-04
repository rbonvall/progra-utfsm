Lanzando monedas
-----------------

Desarrolle un programa
que permite poder simular
el lanzamiento de una moneda,
utilizando la generación de números
aleatorios entre *0* y *1*,
lo cual se puede realizar de la siguiente
forma

::

   import random

   # valor n generado entre 0 y 1
   n = random.random()

Como ya posee el mecanismo para realizarlo,
ahora debe simular el lanzamiento de 500 monedas
y poder desplegar por pantalla la cantidad
de *caras* y *sellos* que obtuvo,
siguiendo la siguiente regla

.. math::

   Si\ n < 0.5:\ sello

   Si\ n \geq 0.5:\ cara


::

   Lanzando monedas...
   Caras: 262
   Sellos: 238
