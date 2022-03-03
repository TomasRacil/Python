# Hodnoty karet
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Třída Card
class Card():
    """
    Ve třídě Card vypisujeme hodnotu a typ karty.
    """

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
        rankstr = self.rank
        suitstr = self.suit
        if self.rank == 'J':
            rankstr = 'Jack'
        elif self.rank == 'Q':
            rankstr = 'Queen'
        elif self.rank == 'K':
            rankstr = 'King'
        elif self.rank == 'A':
            rankstr = 'Ace'
        if self.suit == 'S':
            suitstr = 'Spades'
        elif self.suit == 'H':
            suitstr = 'Hearts'
        elif self.suit == 'C':
            suitstr = 'Clubs'
        elif self.suit == 'D':
            suitstr = 'Diamonds'
        return "{x} of {y}".format(x=rankstr, y=suitstr)
