from os import path


class Card:
    def __init__(self, card):
        '''
        card creation converting string to 2d field
        param: str card
        '''
        self.pole = [[int(num) for num in line.split()]
                     for line in card.split("\n")]
        self.won = False

    def __repr__(self):
        """
        print card representation
        """
        for line in self.pole:
            print(line)

    def removeNumber(self, number):
        """
        param: int - number to be crosed from card
        """
        for line in self.pole:
            if number in line:
                line[line.index(number)] = None

    def checkCompletion(self):
        """
        check if card is completed
        return: bool
        """
        for line in self.pole:
            if len(set(line)) <= 1:
                self.won = True
                return True
        for i in range(len(self.pole[0])):
            if len(set([row[i] for row in self.pole])) <= 1:
                self.won = True
                return True
        else:
            return False

    def sumOfNumbers(self):
        """
        return sum of all non crosed numbers on card
        return: int
        """
        return(
            sum([sum([num for num in line if num is not None])
                for line in self.pole])
        )


with open(path.join(
        path.dirname(path.realpath(__file__)),
        "input.txt"), "r") as inp:
    # creates list of draws
    draws = [int(num) for num in inp.readline().split(",")]
    # creates list of Card objects
    cards = [Card(card) for card in inp.read().strip().split("\n\n")]

pocetViteznychKaret = 0
# going through all draws and cards if card is complete
# check how many cards were already completed
# if 1 or all cards were completed
# print sum of remining numbers*number of draws
for draw in draws:
    for card in cards:
        card.removeNumber(draw)

        if card.checkCompletion():
            temp = len([card for card in cards if card.won])
            if pocetViteznychKaret != temp:
                pocetViteznychKaret = temp
                if (pocetViteznychKaret == 1 or
                        pocetViteznychKaret == len(cards)):
                    print(f"{pocetViteznychKaret}: {card.sumOfNumbers()*draw}")

    if pocetViteznychKaret == len(cards):
        break
