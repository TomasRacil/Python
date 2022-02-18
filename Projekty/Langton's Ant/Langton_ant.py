import turtle #dokumentace: https://docs.python.org/3.3/library/turtle.html
import time
  

 #header
print("Program \"Langtonův mravenec\"")

    #buďto se spouští předefinované nastavení nebo si můžeme nastavení upravit sami
def main():

    nastaveni = input("Přejete si vstoupit do nastavení? [y/n]")

    if nastaveni == 'y':
        print("Jste v nastavení.")
        AntModified()

    elif nastaveni == 'n':
        print("Pokračujeme s přednastavenými hodnotami!")
        delay()
        Ant()
       
    else:
        Chyba()
       

def settings():
    print("Výběr barev: \n [ yellow, gold, orange, red, maroon, \nviolet, magenta, purple, navy, blue, \nskyblue, cyan, turquoise, lightgreen, green, \ndarkgreen, chocolate, brown, black, gray, white]\n")
    ScreenColor = str(input("Zadejte barvu pozadí: "))
    AntFillColor = str(input("Zadejte barvu mravence: ")) #barva políček
    AntSpeed = int(input("Zadejte rychlost [1-10]; nejpomalejší 1, nejrychlejší 10]: ")) # slowest 1; fastest 10 -> funkce Speed
    return ScreenColor, AntFillColor, AntSpeed

def Ant():

    #načtení plátna, barva pozadí a velikost plátna
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(2000,2000)

    # slovník pro uložení souřadnice a barvy
    maps = {}
    # vytvoření grafického mravence, určení tvaru a velikosti
    ant = turtle
    ant.shape('square')    
    ant.shapesize(0.5)
      
    ant.speed(10)   # rychlost mravence     
    ant.tracer(2,0)     # pro zrychlení ruší VSync - plátno se neobnovuje s frekvencí obrazovky -> parametry: (počet přeskočených obnov, zpoždění)                          
    pos = coordinate(ant)   # přiřazení souřadnice pro mravence -> funkce coordinate                                    

    for i in range(12000):      #mravenec začíná dělat dálnici cca po 11000 cyklech, jinak program běží do nekonečna
          
        step = 10   # vzdálenost jakou mravenec urazí
        #pokud mravenec ještě danou pozici nenavštívil a nebo je pozice bílá, změní se barva na černou, mravenec se otočí doprava a posune se                            
        if pos not in maps or maps[pos] == "white":
            ant.fillcolor("black")         
            ant.stamp() # udělá kopii mravence na plátno     
            invert(maps, ant, "black")
            ant.right(90)  # otočí mravence doprava
            ant.forward(step) # posune mravence o jeden krok dopředu
            pos = coordinate(ant) #uloží pozici

        # pokud je pozice černá, mravenec změní barvu na bílou, otočí se doleva a udělá krok dopředu      
        elif maps[pos] == "black":
            ant.fillcolor("white")
            invert(maps, ant, "white")
            ant.stamp()
            ant.left(90)
            ant.forward(step)
            pos = coordinate(ant)

    turtle.done()  #nezavírá plátno po dokončení cyklů

def AntModified():
    ScreenColor, AntFillColor,  AntSpeed = settings()
    delay()
    window = turtle.Screen()
    window.bgcolor(ScreenColor)
    window.screensize(2000,2000)
    maps = {}

    ant = turtle
    ant.shape('square')    
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
  
#funkce získává aktuální pozici mravence
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))

#časový odpočet načtení (nemá žádnou reálnou funkci, pouze doplněk)
def delay():
    print("Nacitam...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

#funkce na rychlost animace, vrací hodnoty do funkce ModifiedAnt
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

#funkce pro chybu vstupu
def Chyba():
    decision = input("Chyba vstupu! Chcete pokračovat? [y/n]: ")
    if decision == "y":
        return main()
    else: 
        return 0



main()