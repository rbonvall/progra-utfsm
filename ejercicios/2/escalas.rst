Escalas
-------

En los juegos de naipes, una carta tiene dos atributos:
un valor (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q o K) y
una pinta (♥, ♠, ♦ o ♣).

En un programa, una carta puede ser representada como una
tupla de dos elementos: el valor y la pinta.
El valor es un numero del 1 al 13, y la pinta es un string ('C', 'P', 'D' o 'T').

Una mano puede ser representada como un conjunto de cartas.
Por ejemplo, uno puede representar
la mano 5♣ 2♥ 1♠ Q♥ K♣ de la siguiente manera:

::

	mano = {(5, 'T'), (2, 'C'), (1, 'P'), (12, 'C'), (13, 'T')}


En el carioca (un juego de naipes chileno) una escala es una
mano de cuatro cartas que tienen la misma pinta y que tienen valores consecutivos.

Por ejemplo:

* 3♥ 6♥ 5♥ 4♥ es una escala, ya que todas las cartas tienen pinta ♥ y valores consecutivos
  desde el 3 hasta el 6.
* 3♣ 6♦ 5♦ 4♥ no es una escala, ya que las cartas tienen pintas diferentes.
* 3♣ A♣ J♣ 5♣ no es una escala, ya que los valores no son consecutivos.
* 3♠ 4♠ 5♠ no es una escala, ya que la mano no tiene cuatro cartas.


Escriba una función *es_escala(mano)* que indique si la mano es una escala o no:

::


	>>> es_escala({(3,'C'), (6, 'C'), (5, 'C'), (4, 'C')})
	True
	>>> es_escala({(3,'T'), (6, 'D'), (5, 'D'), (4, 'C')})
	False
	>>> es_escala({(3,'T'), (1, 'T'), (11, 'T'), (5, 'T'))
	False
	>>> es_escala({(3,'C'), (4, 'C'), (5, 'C')})
	False
