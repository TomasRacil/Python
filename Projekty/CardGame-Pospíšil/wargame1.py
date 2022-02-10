import random

# Rozdělení karet
suits=['S','H','C','D']
ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# Hodnoty karet
values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

# Třída Card
class Card():

    def __init__(self, rank, suit):
        """
        Inicializujeme atributy rank a suit
        """
        self.rank = rank
        self.suit = suit

    def getValue(self):
        """
        Funkce vrací hodnotu karty.
        """
        return values[self.rank]


    def __str__(self):
        """
        Po vyvolání vypíše místo hodnoty slovo.
        Vrátí mi hodnotu a typ karty.
        """
        rankstr=self.rank
        suitstr=self.suit
        if self.rank == 'J':
            rankstr='Jack'
        elif self.rank =='Q':
            rankstr='Queen'
        elif self.rank =='K':
            rankstr='King'
        elif self.rank =='A':
            rankstr='Ace'
        if self.suit == 'S':
            suitstr='Spades'
        elif self.suit == 'H':
            suitstr='Hearts'
        elif self.suit == 'C':
            suitstr='Clubs'
        elif self.suit == 'D':
            suitstr='Diamonds'
        return "{x} of {y}".format(x=rankstr,y=suitstr)

class Deck():

    def __init__(self): 
        """
        Funkce rozděluje karty na Spades, Hearts, Clubs, Diamonds.
        Když jsou karty rozdělené, tak je pomocí RANDOM zamíchá.
        """
        self.cards=[]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def __str__(self):
        """
        Přiřazuje kartu hráči.
        """
        for card in self.cards:
            print(card)
        return ('')

    def __len__(self):
        """
        Vrací hodnotu: počet karet v balíčku.
        """
        return len(self.cards)

    def deal_card(self):
        """
        Rozdá kartu (Vyhazuje kartu z celkového balíčku).
        """
        return self.cards.pop()

class Hand():

    def __init__(self,playername):
        """
        Inicializujeme atributy mycards a playername
        """
        self.mycards=[]
        self.playername = playername

    def __str__(self):
        """
        Vypíše kartu hráče.
        """
        for card in self.mycards:
            print (card)
        return ('')

    def __len__(self):
        """
        Kontrola počtu karet v balíčku hráče.
        """
        return len(self.mycards)

    def add_card(self,card):
        """
        Přidá kartu hráči. (Vkládá kartu do balíčku hráče).
        """
        self.mycards.append(card)


def playcards(hand1, hand2, warcards=[]):
    """
    Funkce počítá s varianout, kdy jeden z hráčů má vyžší kartu a druhý nižší, ale také
    s variantou války, které se vyvolá ve chvíli, když se karty svoji hodnotou rovnají.
    """
    card1=hand1.mycards.pop()
    card2=hand2.mycards.pop()

    print("{a}: {b}".format(a=player1name, b=card1))
    print("{c}: {d}".format(c=player2name, d=card2))

    print('')


    # Když se karty rovnají, tak válka, jinak 2 varianty - vítěz 1.hráč/2.hráč
    if card1.getValue() == card2.getValue(): 
        print('WAR!!!')
        print('')
        war(hand1, hand2, card1, card2)
    elif card1.getValue() > card2.getValue(): 
        print("{a} wins!".format(a=player1name))
        hand1.mycards.insert(0,card1)       # insert vloží zadanou hodnotu na zadanou pozici
        hand1.mycards.insert(0,card2)
        for card in warcards:
            hand1.mycards.insert(0,card)
    else:
        print("{b} wins!".format(b=player2name))
        hand2.mycards.insert(0,card1)
        hand2.mycards.insert(0,card2)
        for card in warcards:
            hand2.mycards.insert(0,card)


def war(hand1, hand2, card1, card2):
    """
    Funkce reprezentuje válku.
    Když hráč č.1 a hráč č.2 mají stejnou kartu (hodnotu karty), tak se pro každého hráče vytvoří list
    do kterého se vloží 3 vrchní karty z jeho balíčku. Potom se karty vypíší a zavolá se funkce PLAYCARDS
    pro porovnání a dosažení výsledku.
    """
    warcards1=[card1]
    warcards2=[card2]
    i=3
    while i>0:
        warcards1.append(hand1.mycards.pop())
        warcards2.append(hand2.mycards.pop())
        i=i-1
    print("Player 1 Cards:")
    for card in warcards1:
        print(card)
    print('')
    print("Player 2 Cards:")
    for card in warcards2:
        print(card)
    
    print('')
        
    
    playcards(hand1, hand2, warcards1 + warcards2)


#START GAME

maindeck=Deck()

player1name=input('Player One:')    # Jméno 1.hráče
hand1=Hand(player1name)             # Karty 1.hráče            

player2name=input('Player Two:')    # Jméno 2.hráče
hand2=Hand(player2name)             # Karty 2. Hráče


# Rozdává karty (skočí až bude balíček karet prázdný).
while len(maindeck)>0:
    hand1.add_card(maindeck.deal_card())
    hand2.add_card(maindeck.deal_card())

# Pokud mají oba hráči, alespoň 1 kartu, tak hra pokračuje, pokud nezbyde hráči karta, hra se ukončí.
while len(hand1)>0 and len(hand2)>0:
    print("\nTime for another round")
    print(player1name+" has "+str(len(hand1.mycards))+" cards")
    print(player2name+" has "+str(len(hand2.mycards))+" cards\n")
    
    playcards(hand1, hand2)

    print('')
    
    # Ukončí běh programu.
    keepplaying=input('Type Q to Quit.  Otherwise, press Enter to Continue  ').upper()
    if keepplaying == 'Q':
        
        break
     