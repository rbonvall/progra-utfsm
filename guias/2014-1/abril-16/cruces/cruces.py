from turtle import *
shape('turtle')
speed('fastest')
def cruz(n):
    for i in range(4):
        forward(n)
        left(90)
        forward(n)
        right(90)
        forward(n)
        right(90)

color('orange')
width(2)
for i in range(6):
    down()
    cruz(30 + 12 * i)
    up()
    left(90)
    forward(6)
    left(90)
    forward(18)
    left(180)

