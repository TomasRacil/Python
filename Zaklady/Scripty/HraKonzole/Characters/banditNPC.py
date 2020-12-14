from .character import *

class banditNPC(character): #za NPC nelze hrát - nemá fce jako heal a sleep
    def __init__(self):
        self.type=4
        self.hp=60
        self.energy=100
        self.damage=50
