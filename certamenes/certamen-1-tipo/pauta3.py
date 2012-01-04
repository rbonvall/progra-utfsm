x = float(raw_input('x: '))
p = float(raw_input('p: '))

suma = 0.0
signo = 1
n = 1
potencia = 1.0
factorial = 1.0
actual = x
anterior = actual + 2 * p # para que entre al ciclo
while abs(actual - anterior) > p:

    suma = suma + actual

    factorial = factorial * (n + 1) * (n + 2)
    n = n + 2
    signo = -signo

    anterior = actual
    actual = signo * (x ** n) / factorial
    #print signo, '* x **', n, '/', factorial

print suma
