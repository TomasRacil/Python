import turtle

"""
Hlavní funkce mravence:
- načte plátno, barvu pozadí a velikost
- vytvoří grafického mravence, určí tvar a velikost a rychlost
- přiřadí souřadnice pro mravence -> funkce coordinate 

Pravidla:
- pokud mravenec ještě danou pozici nenavštívil a nebo je pozice bílá, změní se barva na černou, mravenec se otočí doprava a posune se
- pokud je pozice černá, mravenec změní barvu na bílou, otočí se doleva a udělá krok dopředu

- mravenec začíná dělat dálnici cca po 11000 cyklech, jinak program běží do nekonečna
"""

def Ant():
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(2000,2000)
    maps = {}   # slovník pro uložení souřadnice a barvy

    ant = turtle
    ant.shape('square')    
    ant.shapesize(0.5)
      
    ant.speed(10)    
    ant.tracer(2,0)  # pro zrychlení ruší VSync - plátno se neobnovuje s frekvencí obrazovky -> parametry: (počet přeskočených obnov, zpoždění)                          
    pos = coordinate(ant)                                   

    for i in range(12000): 
          
        step = 10                           
        if pos not in maps or maps[pos] == "white":
            ant.fillcolor("black")         
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

    turtle.done()  #nezavírá plátno po dokončení cyklů

    # funkce mění barvu v závislosti na vstupní barvě
def invert(graph, ant, color):
    graph[coordinate(ant)] = color
  
# funkce získává aktuální pozici mravence
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))
    
