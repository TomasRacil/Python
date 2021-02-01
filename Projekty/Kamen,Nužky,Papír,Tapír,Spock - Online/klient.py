import pygame
from síť import Sit 
import pickle
pygame.font.init() #seznam všech systémových funkcí

width = 700
height = 700
okno = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

class Tlačítko:
	def __init__(self,text,x,y,barva):
		self.text=text
		self.x=x
		self.y=y
		self.barva=barva
		self.width = 150
		self.height = 50

	def vykreslit(self,okno):
		pygame.draw.rect(okno,self.barva,(self.x,self.y,self.width,self.height))
		font = pygame.font.SysFont("somicsans",40) #systémový font písma
		text = font.render(self.text,1, (255,255,255)) #tímhle generujeme font
		okno.blit(text, (self.x+ round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
	def kliknuti(self,pozice): #říká nám zda bylo kliknuto na tlačítko (sleduje polohu miši jestli je v rozmezí tlačítka)
         x1 = pozice[0]
         y1 = pozice[1]
         if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
         else :
            return False

def prekreslovaciOkno(okno, hra, p):
    okno.fill((128,128,128))
   
    if not(hra.pripojeni()): #pokud není druhý hráč připojen
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Čeká se na hráče...", 1, (0,0,255), True)
        okno.blit(text,(width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Ty", 1, (0, 255,255))
        okno.blit(text, (80, 200))

        text = font.render("Protihráč", 1, (0, 255, 255))
        okno.blit(text, (380, 200))

        tah1 = hra.dostan_tah_hrace(0)
        tah2 = hra.dostan_tah_hrace(1)
        if hra.obaWent(): #pokud oba odešli můžeme ukazat jejich tahy
            text1 = font.render(tah1, 1, (0,0,0))
            text2 = font.render(tah2, 1, (0, 0, 0))
        else:
            if hra.p1Went and p == 0: #muj tah
                text1 = font.render(tah1, 1, (0,0,0))
            elif hra.p1Went: #protihračuv tah(hrače jedna když my nejsme hrač 1)
                text1 = font.render("Již Táhl", 1, (0, 0, 0))
            else: #pokud ještě nehrál protihráč(hráč1)
                text1 = font.render("Vybírá...", 1, (0, 0, 0))

            if hra.p2Went and p == 1: #hráč dvě
                text2 = font.render(tah2, 1, (0,0,0)) #pokud jsem hráč dvě já
            elif hra.p2Went: #ja nejsem hrač 2 a on už tahl
                text2 = font.render("Již Táhl", 1, (0, 0, 0))
            else: #hrač 2 vybírá
                text2 = font.render("Vybírá...", 1, (0, 0, 0))

        if p == 1: #pokud jsme hráč 2
            okno.blit(text2, (100, 350)) #nas tah
            okno.blit(text1, (400, 350)) #protivnikuv tah
        else:
            okno.blit(text1, (100, 350)) #nas tah(hrač1)
            okno.blit(text2, (400, 350)) #protihračuv tah

        for tlacidlo in tlačítka:
            tlacidlo.vykreslit(okno)

    pygame.display.update()
tlačítka = [Tlačítko("Kámen", 50, 500, (0,0,0)), Tlačítko("Nůžky", 250, 500, (255,0,0)), Tlačítko("Papír", 450, 500, (0,255,0)), Tlačítko("Tapír",50,600,(0,0,255)), Tlačítko("Spock",250,600,(255,0,255))]
def main():
    run = True
    clock = pygame.time.Clock() #skrze fps 
    n = Sit() #importujeme network 
    hrac = int(n.ziskejP())
    print("Jsi hráč:", hrac)

    while run:
        clock.tick(60)
        try:
            hra = n.send("get") #potřebujeme aby jsme získavali každý rámec info ze serveru
        except:
            run = False
            print("Hra se nespustila")
            break

        if hra.obaWent(): #pokud oba odejdou
            prekreslovaciOkno(okno, hra, hrac)
            pygame.time.delay(500) #zpoždění "jestli opravdu oba odešli"
            try:
                hra = n.send("reset")
            except:
                run = False
                print("Hra se nespustila")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (hra.vitez() == 1 and hrac == 1) or (hra.vitez() == 0 and hrac == 0):
                text = font.render("Vyhrál jsi!", 1, (255,0,0))
            elif hra.vitez() == -1: #pokud je remíza
                text = font.render("Remíza!", 1, (255,0,0)) 
            else:
                text = font.render("Prohrál jsi...", 1, (255, 0, 0))

            okno.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2)) #aby text byl na středu
            pygame.display.update() #updatujeme display textem
            pygame.time.delay(2000) #zpoždění 2s

        for event in pygame.event.get(): #aby jsme mohli ukončit křížkem
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                pozice = pygame.mouse.get_pos()
                for tlačítko in tlačítka:
                    if tlačítko.kliknuti(pozice) and hra.pripojeni(): #pokud klikneme a jsme připojeni
                        if hrac == 0:
                            if not hra.p1Went: #pokud tu je hrač1
                                n.send(tlačítko.text) #pošleme mu text tlačítek
                        else:
                            if not hra.p2Went:
                                n.send(tlačítko.text)

        prekreslovaciOkno(okno, hra, hrac) #aktualizace okna
def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        okno.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Klikni a hraj!", 1, (255,0,0))
        okno.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()




