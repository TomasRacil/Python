class Hand():
    
    """Ve třídě Hand vypisujeme a přidáváme hráči kartu, kontrolujeme počet karet v balíčku"""

    def __init__(self, playername):
        """
        Inicializujeme atributy mycards a playername
        """
        self.mycards = []
        self.playername = playername

    def __str__(self):
        """
        Vypíše kartu hráče.
        """
        for card in self.mycards:
            print(card)
        return ('')

    def __len__(self):
        """
        Kontrola počtu karet v balíčku hráče.
        """
        return len(self.mycards)

    def add_card(self, card):
        """
        Přidá kartu hráči. (Vkládá kartu do balíčku hráče).
        """
        self.mycards.append(card)