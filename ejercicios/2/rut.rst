Rol único tributario (RUT)
--------------------------

El RUT es el número con el cual es posible identificar
a cualquier persona en Chile.

Dentro de su estructura posee un dígito verificador,
que es calculado considerando el resto de los números
antes del guión, sirviendo principalmente para evitar
engaños y suplantaciones de identidad.

Los pasos para obtener el dígito verificador son los siguientes:

* Considere un RUT sin dígito verificador:

::

	11223344-?

* Ahora procedemos a multiplicarlos por la siguiente secuencia de números:

::

	2, 3, 4, 5, 6, 7

Si se nos acaban comenzamos denuevo la secuencia.

La multiplicación se hace considerando los elementos del RUT de derecha a izquierda:

.. math::

	4\times 2 = 8 
	4\times 3 = 12
	3\times 4 = 12
	3\times 5 = 15
	2\times 6 = 12
	2\times 7 = 14
	1\times 2 = 2
	1\times 3 = 3

* Considerando los resultados de la multiplicación,
  ahora procedemos a sumarlos.

::

	8 + 12 + 12 + 15 + 12 + 14 + 2 + 3 = 78

* Con el resultado de la suma, ahora se debe obtener el resto
  de la división por 11. (recuerde el módulo `%`)

::

	78 % 11 = 1

* Ahora restamos a 11 el resto obtenido:

::

	11 - 1 = 10

* Con el resultado, ustede debe verificar las siguiente condiciones
  para que finalmente encuentre el *dígito verificador*:


 * Si el número obtenido es 1, 2, 3, 4, 5, 6, 7, 8 ó 9,
   ése es el dígito verificador.
 * Si el número obtenido es 11,
   el dígito verificador es 0.
 * Si el número obtenido es 10,
   el dígito verificador es K.

* Por lo tanto nuestro RUT será:

::

	11223344-k


Ahora, luego de comprender como calcular el dígito verificador,
realice una función que permita validar un rut ingresado por el usuario,
llamada *valida_rut(rut)*.

::

	valida_rut(11223344-2)
	False

::

	valida_rut(11223344-k)
	True

