def contar_letras(palabra):
    cuentas = {}
    for letra in palabra:
        if letra not in cuentas:
            cuentas[letra] = 0
        cuentas[letra] = cuentas[letra] + 1
    return cuentas

