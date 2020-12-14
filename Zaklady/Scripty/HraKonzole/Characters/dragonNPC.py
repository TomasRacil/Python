from .character import *

class dragonNPC(character): #za NPC nelze hrát - nemá fce jako heal a sleep
    def __init__(self):
        self.type=5
        self.hp=200
        self.energy=20
        self.damage=80
