"""
Langtonův mravenec
    - dvourozměrný univerzální Turingův stroj s jednoduchým souborem pravidel, ale komplexním chováním
"""

import turtle # dokumentace: https://docs.python.org/3.3/library/turtle.html
from modules import Ant as ant
from modules import Delay 

print('Program \"Langtonův mravenec\"')

# Hlavní funkce spouští varianty - s nastavením/bez nastavení
def main():

    nastaveni = input("Přejete si vstoupit do nastavení? [y/n] ")

    if nastaveni == "y":
        print("Jste v nastavení.")
        AntModified()

    elif nastaveni == "n":
        print("Pokračujeme s přednastavenými hodnotami!")
        Delay.delay()
        ant.Ant()
       
    else:
        Chyba()
       

#Funkce nastavení - uživatel vybírá barvy a rychlost mravence       
def settings():
    print("Výběr barev: \n[yellow, gold, orange, red, maroon, \nviolet, magenta, purple, navy, blue, \nskyblue, cyan, turquoise, lightgreen, green, \ndarkgreen, chocolate, brown, black, gray, white]\n")
    ScreenColor = str(input("Zadejte barvu pozadí: "))
    AntFillColor = str(input("Zadejte barvu mravence: "))
    AntSpeed = int(input("Zadejte rychlost [1-10]; nejpomalejší 1, nejrychlejší 10]: "))
    return ScreenColor, AntFillColor, AntSpeed

# Varianta funkce ant kdy uživatel zadává nastavení
def AntModified():
    ScreenColor, AntFillColor,  AntSpeed = settings()
    Delay.delay()
    window = turtle.Screen()
    window.bgcolor(ScreenColor)
    window.screensize(2000,2000)
    maps = {}

    ant = turtle
    ant.shape("square")    
    ant.shapesize(0.5)
      
    ant.speed(AntSpeed)     

    Speed(AntSpeed,ant)
    
    pos = coordinate(ant)                               

    for i in range(12000):  
          
        step = 10
        if pos not in maps or maps[pos] == "white":
            ant.fillcolor(AntFillColor)         
            ant.stamp()  
            invert(maps, ant, "black")
            ant.right(90)
            ant.forward(step)
            pos = coordinate(ant)

        elif maps[pos] == "black":
            ant.fillcolor("white")
            invert(maps, ant, "white")
            ant.stamp()
            ant.left(90)
            ant.forward(step)
            pos = coordinate(ant)

    turtle.done()


# funkce mění barvu v závislosti na vstupní barvě
def invert(graph, ant, color):
    graph[coordinate(ant)] = color
  
# funkce získává aktuální pozici mravence
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))

# časový odpočet z modulu - (nemá žádnou reálnou funkci, pouze doplněk)
Delay.delay()

# funkce na rychlost animace, vrací hodnoty do funkce ModifiedAnt
def Speed(AntSpeed, ant):

    if AntSpeed == 1:
        return ant.speed(1), ant.delay(50)
    elif AntSpeed == 2:
        return ant.speed(1),
    elif AntSpeed == 3:
        return ant.speed(2)
    elif AntSpeed == 4:
        return ant.speed(3)
    elif AntSpeed == 5:
        return ant.speed(4)
    elif AntSpeed == 6:
        return ant.speed(6)
    elif AntSpeed == 7:
        return ant.speed(10)
    elif AntSpeed == 8:
        return ant.speed(10), ant.tracer(2,0)
    elif AntSpeed == 9:
        return ant.speed(10), ant.tracer(8,0)
    elif AntSpeed == 10:
        return ant.speed(10), ant.tracer(60,0)    
    else:
        print("Zadali jste neznámou hodnotu!")
        return AntModified()

# funkce pro chybu vstupu
def Chyba():
    decision = input("Chyba vstupu! Chcete pokračovat? [y/n]: ")
    if decision == "y":
        return main()
    else: 
        return 0

if __name__ == '__main__':
    main()
