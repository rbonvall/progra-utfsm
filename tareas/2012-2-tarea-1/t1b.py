import turtle

turtle.title('Laberinto')
turtle.shape('turtle')
turtle.color('brown')
turtle.width(5)
turtle.speed('fastest')

f = 30


fila = ':)'
y = 0
while len(fila) > 0:
    fila = raw_input('> ')
    n = len(fila)
    for x in range(n):
        if fila[x] == 'x' or fila[x] == 'X':
            turtle.up()
            turtle.goto(f * x, f * y)
            turtle.seth(90)
            turtle.down()
            for i in range(4):
                turtle.forward(f)
                turtle.right(90)
    y -= 1

turtle.up()
turtle.goto(-f / 2, +f / 2)
turtle.seth(0)
turtle.down()
turtle.color('navy')
turtle.width(2)
turtle.speed('slowest')

ruta = raw_input('Ruta: ')
n = len(ruta)
for i in range(n):
    d = ruta[i]
    if   d == 'E': turtle.seth(0)
    elif d == 'N': turtle.seth(90)
    elif d == 'O': turtle.seth(180)
    elif d == 'S': turtle.seth(270)
    turtle.forward(f)

print 'Distancia recorrida:', len(ruta)
raw_input()

