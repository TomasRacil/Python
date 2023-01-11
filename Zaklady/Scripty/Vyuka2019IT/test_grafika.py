import turtle
from math import sqrt

rozmer = 100

print(turtle.position())
turtle.forward(rozmer)
turtle.backward(rozmer/2)
turtle.left(90)
turtle.forward(int(rozmer*1.5))
turtle.backward(int(rozmer*1.5-rozmer/2))
turtle.left(135)
turtle.forward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
turtle.backward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
turtle.left(90)
turtle.forward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
turtle.backward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
turtle.left(135)
turtle.forward(int(rozmer*1.5-rozmer/2))
turtle.left(90)
turtle.forward(rozmer)
turtle.left(90)
turtle.forward(rozmer/2)
turtle.right(90)
turtle.circle(rozmer/10)
turtle.circle(rozmer/10,180)
turtle.right(90)
turtle.forward(50)
input()