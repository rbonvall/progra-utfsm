Países
------

El diccionario ``paises`` asocia cada persona
con el conjunto de los países que ha visitado::

    paises = {
        'Pepito': {'Chile', 'Argentina'},
        'Yayita': {'Francia', 'Suiza', 'Chile'},
        'John': {'Chile', 'Italia', 'Francia', 'Peru'},
    }

Escriba una funcion ``cuantos_en_comun(a, b)``,
que indique cuántos países en común han visitado
la persona ``a`` y la persona ``b``::

    >>> cuantos_en_comun('Pepito', 'John')
    1
    >>> cuantos_en_comun('John', 'Yayita')
    2

