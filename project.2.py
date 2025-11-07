from myfunctions import*

from random import*
turtle.colormode(255)
turtle.bgcolor("black")
turtle.tracer(False)

def shape(angle):
    for times in range(200):
        bob.forward(times)
        bob.right(angle)
        bob.color(140,times,140)
        bob.left(7)
for times in range(90):
    jump(-1000 + times * 200,0)
    shape(600)

for times in range(90):
    jump(-1000 + times * 200, -200)
    shape(600)
for times in range(90):
    jump(-1000 + times * 200, -400)
    shape(600)
for times in range(90):
    jump(-1000 + times * 200, 200)
    shape(600)
for times in range(90):
    jump(-1000 + times * 200, 400)
    shape(600)
