Polinomios, evaluación y derivación
-----------------------------------

Realice un programa que sea capaz
de poder realizar los siguientes
puntos, considerando el siguiente
polinomio.

.. math::

	p(x) = \alpha \cdot x^{n} + \beta \cdot x^{n-1} + \ldots + \gama \cdot x + \theta

* Lea los coeficientes del polinomio de grado *n*.
  Esto implica poder leer tanto *n* como todos los coeficientes.
* Evalue `p(x)` en `x = x_{0}` y presente el resultado.
  `x_{0}` debe ser ingresado por el usuario.
* Obtenga la expresion `p'(x)`.
* Evalue `p'(x)` en `x = x_{0}` y presente el resultado.

Recuerde que puede representar el polinomio `p(x)` como
una lista con los coeficientes.

::

	Ingrese n: 3
	Coeficiente 1: 2
	Coeficiente 2: 4
	Coeficiente 3: -1
	Coeficiente 4: 7
	Polinomio: 2 * x^3 + 4 * x^2 - 1 * x + 7
	Ingrese x0: 0
	p(0) = 7
	Derivada: 6 * x^2 + 8 * x - 1
	p'(0) = -1
