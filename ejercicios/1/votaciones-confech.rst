Votaciones de la CONFECH
========================

*Este problema apareció en el certamen 1 del segundo semestre de 2011 en el campus Vitacura.*

La CONFECH,
en su afán de agilizar el proceso de recuento de las votaciones,
le ha encargado el desarrollo de un programa de registro de votación por universidades.

Primero, el programa debe solicitar al usuario ingresar
la cantidad de universidades que participan en el proceso.

Luego, para cada una de las universidades,
el usuario debe ingresar
el nombre de la universidad
y los votos de sus alumnos, que pueden ser:
*aceptar*  (``A``),
*rechazar* (``R``),
*nulo*     (``N``) o
*blanco*   (``B``).
El término de la votación se indica ingresando una ``X``,
tras lo cual se debe mostrar los totales de votos de la universidad,
con el formato que se muestra en el ejemplo.

Finalmente,
el programa debe mostrar el resultado de la votación,
indicando la cantidad de universidades que aceptan, que rechazan
y en las que hubo empate entre estas dos opciones.

.. testcase::

    Numero de universidades: `3`

    Universidad: `USM`
    Voto: `A`
    Voto: `R`
    Voto: `A`
    Voto: `N`
    Voto: `X`
    USM: 2 aceptan, 1 rechazan, 0 blancos, 1 nulos.

    Universidad: `UChile`
    Voto: `A`
    Voto: `B`
    Voto: `A`
    Voto: `X`
    UChile: 2 aceptan, 0 rechazan, 1 blancos, 0 nulos.

    Universidad: `PUC`
    Voto: `A`
    Voto: `R`
    Voto: `R`
    Voto: `A`
    Voto: `X`
    PUC: 2 aceptan, 2 rechazan, 0 blancos, 0 nulos.

    Universidades que aceptan: 2
    Universidades que rechazan: 0
    Universidades con empate: 1

