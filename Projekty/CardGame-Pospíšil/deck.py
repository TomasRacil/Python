from card import Card
import random

# Rozdělení karet
suits = ['S', 'H', 'C', 'D']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Deck():
    """
    Třída Deck rozděluje a míchá karty, které pak přiděluje hráčům a vrací počet karet v balíčku.
    """

    def __init__(self):
        """
        Funkce rozděluje karty na Spades, Hearts, Clubs, Diamonds.
        Když jsou karty rozdělené, tak je pomocí RANDOM zamíchá.
        """
        self.cards = []
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