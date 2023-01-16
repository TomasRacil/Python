import turtle
from math import sqrt

rozmer = 100
def draw_hangman(erroR_number:int)->None:
    match erroR_number:
        case 1: 
            turtle.forward(rozmer)
            turtle.backward(rozmer/2)
        case 2: 
            turtle.left(90)
            turtle.forward(int(rozmer*1.5))
            turtle.backward(int(rozmer*1.5-rozmer/2))
        case 3:
            turtle.left(135)
            turtle.forward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
            turtle.backward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
        case 4:
            turtle.left(90)
            turtle.forward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
            turtle.backward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
        case 5:
            turtle.left(135)
            turtle.forward(int(rozmer*1.5-rozmer/2))
        case 6:
            turtle.left(90)
            turtle.forward(rozmer)
            turtle.backward(rozmer/2)
        case 7:
            turtle.left(135)
            turtle.forward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
            turtle.backward(int(sqrt((rozmer/2)**2+(rozmer/2)**2)))
            turtle.right(135)
            turtle.forward(rozmer/2)
        case 8:
            turtle.left(90)
            turtle.forward(rozmer/2)
        case 9:
            turtle.right(90)
            turtle.circle(rozmer/10)
            turtle.circle(rozmer/10,180)
        case 10:
            turtle.right(90)
            turtle.forward(rozmer/3)
        case 11:
            turtle.right(45)
            turtle.forward(rozmer/3)
            turtle.backward(rozmer/3)
        case 12:
            turtle.left(90)
            turtle.forward(rozmer/3)
            turtle.backward(rozmer/3)
            turtle.left(135)
            turtle.forward(rozmer/3)
        case 13:
            turtle.right(135)
            turtle.forward(rozmer/3)
            turtle.backward(rozmer/3)
        case 14:
            turtle.right(90)
            turtle.forward(rozmer/3)
            turtle.backward(rozmer/3)