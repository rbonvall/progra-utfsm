Fechas
======

Una fecha puede ser representada como una tupla
``(anno, mes, dia)``.

1. Escriba la función ``dia_siguiente(f)``
   que reciba como parámetro una fecha ``f``
   y entegue cuál es la fecha siguiente::

     >>> dia_siguiente((2011, 4, 11))
     (2011, 4, 12)
     >>> dia_siguiente((2011, 4, 30))
     (2011, 5, 1)
     >>> dia_siguiente((2011, 12, 31))
     (2012, 1, 1)

   Como recomendación,
   dentro de su función use una lista
   con la cantidad de días que tiene cada mes::

     dias_mes = [31, 28, 31, 30,
                 31, 30, 31, 31,
                 30, 31, 30, 31]

2. Escriba la función ``dias_entre(f1, f2)``
   que retorne la cantidad de días
   que han transcurrido entre las fechas ``f1`` y ``f2``::

     >>> hoy = (2011, 4, 11)
     >>> navidad = (2011, 12, 25)
     >>> dias_entre(hoy, navidad)
     258
     >>> dias_entre(hoy, hoy)
     0

3. Escriba un programa que le diga al usuario
   cuántos días de edad tiene:

   .. testcase::

      Ingrese su fecha de nacimiento.
      Dia: `14`
      Mes: `5`
      Anno: `1990`
      Ingrese la fecha de hoy.
      Dia: `20`
      Mes: `4`
      Anno: `2011`
      Usted tiene 7646 dias de edad

