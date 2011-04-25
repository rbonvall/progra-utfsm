Distancias
----------
La siguiente tabla
indica las distancias entre algunas ciudades chilenas:

  ============= ========== ========== ========== ============ ==========
  **Distancia** Arica      Santiago   Valparaíso San Fernando Temuco
  Arica                  0       2050       2015         2190       2725
  Santiago            2050          0        119          140        675
  Valparaíso          2015        119          0          255        790
  San Fernando        2190        140        255            0        535
  Temuco              2725        675        790          535          0
  ============= ========== ========== ========== ============ ==========

En un programa,
esta información puede representarse
mediante un arreglo de ciudades
y un arreglo bidimensional de distancias.

* Escriba la función que pregunte al usuario
  la cantidad de ciudades y los nombres de las ciudades:

  .. code-block:: none

       ¿Cuántas ciudades?
      5
       Ingrese los nombres:
      Arica
      Santiago
      Valparaíso
      San Fernando
      Temuco

* Escriba la función que pregunte al usuario
  las distancias entre cada par de ciudades:

  .. code-block:: none

      ¿Distancia Arica-Santiago?
     2050
      ¿Distancia Arica-Valparaíso?
     2015
     ...
      ¿Distancia Temuco-San Fernando?
     535

  Tener la precaución de preguntar sólo una vez cada par de ciudades:
  si se pregunta Arica-Santiago, no debe preguntarse Santiago-Arica.
  Tampoco debe preguntarse la distancia desde una ciudad a sí misma.

* Escriba la función que pida al usuario
  que ingrese una lista de ciudades,
  que representan un itinerario por realizar:

  .. code-block:: none

      ¿Cuántas ciudades tiene el itinerario?
     4
      Ingrese las ciudades del itinerario:
     Temuco
     Santiago
     San Fernando
     Arica

* Escriba la función ``kms`` que entregue como resultado
  los kilómetros que hay que recorrer para visitar las ciudades en orden.
  Por ejemplo, para el itinerario de arriba,
  debe entregar como resultado `3005`.

