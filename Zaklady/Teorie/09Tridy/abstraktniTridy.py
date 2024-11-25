"""
Abstraktní třídy
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        print('Animal moves')

class Turtle():
    @abstractmethod
    def move(self):
        pass


class Cat(Animal):
    def move(self):
        super().move()
        print('Cat moves')

try:
	a = Animal() 
except Exception as e:
	print(e)

a = Turtle()

c = Cat()
c.move()

# Animal moves
# Cat moves