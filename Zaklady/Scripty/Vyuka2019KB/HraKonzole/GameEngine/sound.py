from playsound import playsound
from GameEngine import *

from os import path

absolute_path = path.dirname(path.abspath(__file__))

def ZvukKostka():
	playsound(absolute_path + '\\soundlib\\kostka.wav')


def ZvukBandita():
	playsound(absolute_path + '\\soundlib\\bandita.wav')


def ZvukDrak():
	playsound(absolute_path + '\\soundlib\\drak.wav')


def ZvukRychlost():
	playsound(absolute_path + '\\soundlib\\rychlost.wav')


def ZvukVoda():
	playsound(absolute_path + '\\soundlib\\voda.wav')


def ZvukSmrt():
	playsound(absolute_path + '\\soundlib\\smrt.wav')
