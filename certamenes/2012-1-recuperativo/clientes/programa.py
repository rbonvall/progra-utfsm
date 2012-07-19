'''
# CASO 1
>>> contar_paises(clientes)
{'Espana': 2, 'Alemania': 1, 'Chile': 3}

# FIN CASO 1

# CASO 2
>>> persona_mas_joven(clientes)
'Pepe Ternero'

# FIN CASO 2

# CASO 3
>>> obtener_mails_cumpleaneros(clientes, 'mayo')
set(['anobel@llahu.de', 'm.m@jemeil.es'])

# FIN CASO 3
'''

# CLIENTES
clientes = [
    ('Pedro', 'Perez',      (1970, 12, 31), 'pperez@hutmail.cl'),
    ('Antonio', 'Nobel',    (1983,  5, 14), 'anobel@llahu.de'),
    ('Marcela', 'Martinez', (1990,  5, 31), 'm.m@jemeil.es'),
    ('Pepe', 'Ternero',     (1995,  3, 12), 'pe.ter.95@ab.xyz.qwe.es'),
    ('Alfonsina', 'Lee',    (1992, 11, 28), 'alee@hutmail.cl'),
    ('Luisa', 'Gonzalez',   (1984,  2, 29), 'lugon@alumnos.usm.cl'),]
# FIN CLIENTES

# PAISES
paises = {
    'es': 'Espana',
    'uk': 'Reino Unido',
    'de': 'Alemania',
    'bw': 'Botswana',
    'cl': 'Chile',
}
# FIN PAISES

# MESES
meses = ['enero', 'febrero', 'marzo', 'abril',
         'mayo', 'junio', 'julio', 'agosto',
         'septiembre', 'octubre', 'noviembre', 'diciembre']
# FIN MESES


def contar_paises(clientes):
    cuentas = {}
    for _, _, _, email in clientes:
        tld = email.split('.')[-1]
        pais = paises[tld]
        if pais not in cuentas:
            cuentas[pais] = 0
        cuentas[pais] += 1
    return cuentas


def persona_mas_joven(clientes):
    fecha_mayor = (0, 0, 0)
    for nombre, apellido, fecha, _ in clientes:
        if fecha > fecha_mayor:
            fecha_mayor = fecha
            joven = nombre + ' ' + apellido
    return joven


def obtener_mails_cumpleaneros(clientes, mes):
    mails = set()
    n_mes = meses.index(mes) + 1
    for _, _, fecha, mail in clientes:
        _, m, _ = fecha
        if n_mes == m:
            mails.add(mail)
    return mails


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)

