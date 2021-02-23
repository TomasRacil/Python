import tkinter as tk
root = tk.Tk()
Round = 1

def VytvorHerniPole(velikostPole, pocetStejnych):
    """
    Vstupy: velikostPole(int): znaci, jak velke bude hraci pole (int) x (int) - pokud je tedy velikostPole např. 5 bude velikost 5x5 (tj. 25 tlacitek) 
            pocetStejnych(int): znaci, kolik stejnych symbolu za sebou je potreba, aby byla uznana vyhra

    Funkce, ktera vytvori libovolne velke pole na zaklade prijatych parametru z mainu
    nejprve do 2d pole vytvori tlacitka pouze se zakladnimi parametry a to v poctu velikost pole x velikost pole
    pote do kazdeho z tlacitek vlozi grid - to je zarovnani (kazde tlacitko je zarovnano do jakesi tabulky)
    pro kazde nastavi command - to je co se stane po zmacknuti tlacitka (lambda je tam protoze nelze napsat Vyhodnot(), protoze by to funkci vykonalo i bez stisku klavesy)
    a v posledni rade nastavi font vsech tlacitek
    """
    global Buttons2D   
    Buttons2D=[[tk.Button(root,width = 10, height = 5, text=" ") for i in range (velikostPole) for i in range (velikostPole)]for j in range(velikostPole)]

   
    for i in range(velikostPole):
        for j in range(velikostPole):
            Buttons2D[i][j].grid(row=i, column=j)
            Buttons2D[i][j]["command"] = lambda i=i,j=j: Vyhodnot(i,j,velikostPole,pocetStejnych)
            Buttons2D[i][j]["font"] = "Helvetica"

def Vyhodnot(r,c,velikostPole, pocetStejnych):
    """
    Vstupy: velikostPole(int): znaci, jak velke bude hraci pole (int) x (int) - pokud je tedy velikostPole např. 5 bude velikost 5x5 (tj. 25 tlacitek) 
            pocetStejnych(int): znaci, kolik stejnych symbolu za sebou je potreba, aby byla uznana vyhra
            r(int): znaci radek, kde se nachazi tlacitko (0 až velikostPole)
            c(int): znaci sloupec, kde se nachazi tlacitko ((0 až velikostPole))

    Funkce, ktera pouze po stisku klavesy zmeni text tlacitka bud na "O" nebo na "X", zalezi jestli je sude nebo liche kolo (round)
    a spousti dalsi funkci (ZkontrolujVyhru), ktere preda parametry
    """
    global Round
    global Buttons2D
    Buttons2D[r][c].config(state="disabled")
    if (Round%2==0):
        Buttons2D[r][c].config(text="O")
        
    else:
        Buttons2D[r][c].config(text="X")
    Round+=1
    ZkontrolujVyhru(r,c, velikostPole, pocetStejnych)

def ZkontrolujVyhru(r, c, velikostPole, pocetStejnych):
    """
    Vstupy: velikostPole(int): znaci, jak velke bude hraci pole (int) x (int) - pokud je tedy velikostPole např. 5 bude velikost 5x5 (tj. 25 tlacitek) 
            pocetStejnych(int): znaci, kolik stejnych symbolu za sebou je potreba, aby byla uznana vyhra
            r(int): znaci radek, kde se nachazi tlacitko (0 až velikostPole)
            c(int): znaci sloupec, kde se nachazi tlacitko ((0 až velikostPole))

    Funkce, ktera kontroluje, zda se nachazi zvoleny pocet "X" nebo "O" za sebou
    Zkontroluje Radky,Sloupce,Hlavni diagonalu z leveho horniho rohu do praveho dolniho, a pote postranni diagonaly
    dale zkontroluje hlavni diagonalu z praveho horniho rohu do leveho dolniho rohu a postanni diagonaly.
    Kontrola probiha tak, ze to zaznamenava pocet X a pocet Y. Pokud je serie jednoho znaku prerusena znakem druhy,
    tak to serii znaku vynuluje. Vynuluje to i pokud dojde for cyklus na konec hraciho pole.
    """
    
    pocetX=0
    pocetO=0

    for i in range (velikostPole):
        for j in range (velikostPole):
            if (Buttons2D[i][j]["text"]==" "):
                pocetX=0
                pocetO=0
            if (Buttons2D[i][j]["text"]=="O"):
                pocetX=0
                pocetO+=1
            if (Buttons2D[i][j]["text"]=="X"):
                pocetX+=1
                PocetO=0
            if (pocetX == pocetStejnych):
                WinLabel=tk.Label(root,text="X - vyhra")
                WinLabel.grid(row=20,column=20)
            if (pocetO == pocetStejnych):
                WinLabel=tk.Label(root,text="O - vyhra")
                WinLabel.grid(row=20,column=20)
            if (j==velikostPole-1):
                pocetX=0
                pocetO=0
               
    
    for i in range (velikostPole):
        for j in range (velikostPole):
            if (Buttons2D[j][i]["text"]==" "):
                pocetX=0
                pocetO=0
            if (Buttons2D[j][i]["text"]=="O"):
                pocetX=0
                pocetO+=1
            if (Buttons2D[j][i]["text"]=="X"):
                pocetX+=1
                pocetO=0
            if (pocetX == pocetStejnych):
                WinLabel=tk.Label(root,text="X - vyhra")
                WinLabel.grid(row=20,column=20)
            if (pocetO == pocetStejnych):
                WinLabel=tk.Label(root,text="O - vyhra")
                WinLabel.grid(row=20,column=20)
            if (j==velikostPole-1):
                pocetX=0
                pocetO=0
    
    
    for i in range (velikostPole):
         if (Buttons2D[i][i]["text"]==" "):
                pocetX=0
                pocetO=0
         if (Buttons2D[i][i]["text"]=="O"):
                pocetX=0
                pocetO+=1
         if (Buttons2D[i][i]["text"]=="X"):
                pocetX+=1
                pocetO=0
         if (pocetX == pocetStejnych):
                WinLabel=tk.Label(root,text="X - vyhra")
                WinLabel.grid(row=20,column=20)
         if (pocetO == pocetStejnych):
                WinLabel=tk.Label(root,text="O - vyhra")
                WinLabel.grid(row=20,column=20)
         if (i==velikostPole-1):
                pocetX=0
                pocetO=0
                  
    
    for k in range (velikostPole):
        j=0  
        for i in range(velikostPole-k):
             if (Buttons2D[i][j+k]["text"]==" "):
                    pocetX=0
                    pocetO=0
             if (Buttons2D[i][j+k]["text"]=="O"):
                    pocetO+=1;
                    pocetX=0
             if (Buttons2D[i][j+k]["text"]=="X"):
                    pocetX+=1
                    pocetO=0
             if (pocetX == pocetStejnych):
                    WinLabel=tk.Label(root,text="X - vyhra")
                    WinLabel.grid(row=20,column=20)
             if (pocetO == pocetStejnych):
                    WinLabel=tk.Label(root,text="O - vyhra")
                    WinLabel.grid(row=20,column=20)
             if (i==velikostPole-k-1):
                    pocetX=0  
                    pocetO=0
             j+=1

      
    for k in range (velikostPole):
        j=0  
        for i in range(velikostPole-k):
             if (Buttons2D[i+k][j]["text"]==" "):
                    pocetX=0
                    pocetO=0
             if (Buttons2D[i+k][j]["text"]=="O"):
                    pocetO+=1
                    pocetX=0
             if (Buttons2D[i+k][j]["text"]=="X"):
                    pocetX+=1
                    pocetO=0
             if (pocetX == pocetStejnych):
                    WinLabel=tk.Label(root,text="X - vyhra")
                    WinLabel.grid(row=20,column=20)
             if (pocetO == pocetStejnych):
                    WinLabel=tk.Label(root,text="O - vyhra")
                    WinLabel.grid(row=20,column=20)
             if (i==velikostPole-k-1):
                    pocetX=0
                    pocetO=0
             j+=1

    
    for k in range (velikostPole):
        j=velikostPole-1 
        for i in range(velikostPole-k):
             if (Buttons2D[i+k][j]["text"]==" "):
                    pocetX=0
                    pocetO=0
             if (Buttons2D[i+k][j]["text"]=="O"):
                    pocetO+=1
                    pocetX=0
             if (Buttons2D[i+k][j]["text"]=="X"):
                    pocetX+=1
                    pocetO=0
             if (pocetX == pocetStejnych):
                    WinLabel=tk.Label(root,text="X - vyhra")
                    WinLabel.grid(row=20,column=20)
             if (pocetO == pocetStejnych):
                    WinLabel=tk.Label(root,text="O - vyhra")
                    WinLabel.grid(row=20,column=20)
             if (i==velikostPole-k-1):
                    pocetX=0
                    pocetO=0
             j-=1
        
    
    
    for k in range (velikostPole):
        j=velikostPole-1 
        for i in range(velikostPole-k):
             if (Buttons2D[i][j-k]["text"]==" "):
                    pocetX=0
                    pocetO=0
             if (Buttons2D[i][j-k]["text"]=="O"):
                    pocetO+=1
                    pocetX=0
             if (Buttons2D[i][j-k]["text"]=="X"):
                    pocetX+=1
                    pocetO=0
             if (pocetX == pocetStejnych):
                    WinLabel=tk.Label(root,text="X - vyhra")
                    WinLabel.grid(row=20,column=20)
             if (pocetO == pocetStejnych):
                    WinLabel=tk.Label(root,text="O - vyhra")
                    WinLabel.grid(row=20,column=20)
             if (i==velikostPole-k-1):
                    pocetX=0
                    pocetO=0
             j-=1