Traslape de rectángulos
=======================

Un rectángulo que está en el plano *xy*
cuyos lados son paralelos a los ejes cartesianos
puede ser representado mediante cuatro datos:

* la coordenada *x* de su vértice inferior izquierdo,
* la coordenada *y* de su vértice inferior izquierdo.
* su ancho *w*, y
* su altura *h*.

.. image:: ../../diagramas/rect.png

En un programa en Python,
esto se traduce en una tupla ``(x, y, w, h)`` de cuatro elementos::

    # el rectangulo de la figura
    rectangulo = (3, 2, 5, 6)

#. Escriba la función ``ingresar_rectangulo()``
   que pida al usuario ingresar los datos de un rectángulo,
   y retorne la tupla con los datos ingresados.
   La función no tiene parámetros.
   Al ejecutar la función,
   la sesión debe verse así:

   .. testcase::

       Ingrese x: `3`
       Ingrese y: `2`
       Ingrese ancho: `5`
       Ingrese alto: `6`

   Con esta entrada, la función retornaría la tupla ``(3, 2, 5, 6)``.

#. Escriba la función ``se_traslapan(r1, r2)``
   que reciba como parámetros dos rectángulos ``r1`` y ``r2``,
   y entregue como resultado si los rectángulos
   se traslapan o no.

   Por ejemplo,
   en el siguiente diagrama,
   los rectángulos A y B se traslapan,
   mientras que los rectángulos A y C no se traslapan:

   .. image:: ../../diagramas/rect2.png

   ::

      >>> a = (1, 8, 8, 5)
      >>> b = (7, 6, 3, 6)
      >>> c = (4, 2, 9, 3)
      >>> se_traslapan(a, b)
      True
      >>> se_traslapan(b, c)
      False
      >>> se_traslapan(a, c)
      False

#. Escriba un programa
   que pida al usuario ingresar varios rectángulos,
   y termine cuando se ingrese uno que se traslape
   con alguno de los ingresados anteriormente.
   La salida debe indicar cuáles son los rectángulos que se traslapan.

   .. testcase::

       Rectangulo 0
       Ingrese x: `4`
       Ingrese y: `2`
       Ingrese ancho: `9`
       Ingrese alto: `3`

       Rectangulo 1
       Ingrese x: `1`
       Ingrese y: `8`
       Ingrese ancho: `8`
       Ingrese alto: `5`

       Rectangulo 2
       Ingrese x: `11`
       Ingrese y: `7`
       Ingrese ancho: `1`
       Ingrese alto: `9`

       Rectangulo 3
       Ingrese x: `2`
       Ingrese y: `6`
       Ingrese ancho: `7`
       Ingrese alto: `1`

       Rectangulo 4
       Ingrese x: `7`
       Ingrese y: `6`
       Ingrese ancho: `3`
       Ingrese alto: `6`
       El rectangulo 4 se traslapa con el rectangulo 1
       El rectangulo 4 se traslapa con el rectangulo 3

#. (¡Difícil!).
   Escriba la función ``contar_regiones_continuas(rectangulos)``
   que reciba como parámetro una lista de rectángulos,
   y retorne la cantidad de regiones continuas formadas
   por rectángulos traslapados.

   Por ejemplo,
   en el siguiente diagrama hay 15 rectángulos
   que forman 6 regiones continuas de rectángulos traslapados:

   .. image:: ../../diagramas/rect3.png

   Los rectángulos de la figura son los siguientes::

    rs = [
        ( 4,  2, 9, 3),
        (14, 10, 5, 1),
        (14, 17, 3, 2),
        (13,  7, 2, 2),
        ( 8, 16, 4, 3),
        (13, 14, 2, 4),
        ( 1,  8, 8, 5),
        ( 1,  1, 6, 4),
        (16, 14, 3, 4),
        (12,  6, 4, 6),
        ( 7,  6, 3, 6),
        ( 5, 15, 4, 3),
        (14, 13, 3, 2),
        (15,  3, 5, 4),
        ( 2, 16, 3, 3),
    ]

   Puede usar esta lista para probar su función::

     >>> contar_regiones_continuas(rs)
     6

