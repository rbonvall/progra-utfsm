Fookbace
========

*Este problema apareció en el certamen 2 del primer semestre de 2011.*

La red social Fookbace
almacena la información de sus usuarios en un diccionario.
Las llaves son un código numérico entero asignado a cada usuario, y
los valores son tuplas
con el nombre, la ciudad y la fecha de nacimiento del usuario.
La fecha de nacimiento es una tupla ``(año, mes, día)``::

  usuarios = {
      522514: ('Jean Dupont',        'Marseille',  (1989, 11, 21)),
      587125: ('Perico Los Palotes', 'Valparaiso', (1990,  4, 12)),
      189471: ('Jan Kowalski',       'Krakow',     (1994,  4, 22)),
      914210: ('Antonio Nobel',      'Valparaiso', (1983,  7,  1)),
      # ...
  }

#. Escriba la función ``misma_ciudad(u1, u2)``,
   que indique si los usuarios con códigos ``u1`` y ``u2``
   viven en la misma ciudad::

    >>> misma_ciudad(914210, 587125)
    True
    >>> misma_ciudad(522514, 189471)
    False

#. Escriba la función ``diferencia_edad(u1, u2)``,
   que retorne la diferencia de edad entre los usuarios
   cuyos códigos son ``u1`` y ``u2``.
   (Utilice sólo el año de nacimiento de los usuarios
   para calcular la diferencia, no el mes ni el día). ::

    >>> diferencia_edad(914210, 587125)
    7

#. Para guardar la información
   sobre cuáles de sus usuarios son amigos entre sí,
   Fookbace utiliza el conjunto ``amistades``,
   que contiene tuplas con los códigos de dos usuarios.
   Si la tupla ``(a, b)`` está dentro del conjunto,
   significa que los usuarios con códigos ``a`` y ``b`` son amigos.
   En todas las tuplas se cumple que ``a`` < ``b``. ::

    amistades = {
        (198471, 289142), (138555, 429900), (349123, 781118), # ...
    }

   #. Escriba la función ``obtener_amigos(u)``,
      que retorne el conjunto de los códigos
      de los amigos de ``u``.
   #. Escriba la función ``recomendar_amigos(u)``,
      que retorne el conjunto de los códigos
      de los usuarios que cumplen todas estas condiciones a la vez:

      * son amigos de un amigo de ``u``,
      * no son amigos de ``u``,
      * viven en la misma ciudad que ``u``, y
      * tienen menos de diez años de diferencia con ``u``.

   En ambas funciones,
   el parámetro ``u`` es el código de un usuario,
   y el valor de retorno es un conjunto de códigos de usuarios.
   Recuerde que ``c.add(x)`` agrega el valor ``x`` al conjunto ``c``.

