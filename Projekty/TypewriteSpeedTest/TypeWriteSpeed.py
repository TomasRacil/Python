# Knihovna pygame - pro grafické rozhraní
import random
import time
import pygame
from pygame.locals import *



class Game:

    def __init__(self):
        self.w = 750        # Velikost okna
        self.h = 600
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Čas:0 Přesnost:0 % WPM:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (0, 255, 170)     # Barva nadpisu
        self.TEXT_C = (240, 240, 240)   # Barva opisované věty
        self.RESULT_C = (0, 255, 0)     # Barva napsané věty

        # Obrázek tlačítka
        pygame.init()
        self.open_img = pygame.image.load('intro.jpg')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        # Obrázek pozadí
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (500, 750))

        # Spuštěné okno
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Rychlost psaní')

        # Pomocná funkce, která zobrazí text na obrazovce
    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()     # Pygame vyžaduje aktualizaci obrazovky po zobrazení čehokoliv

        # Zajistíme otevření souboru s větami a získání náhodného řádku
    def get_sentence(self):
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    # Jakmile uživatel klikne do psacího pole, začne se počítat čas. Po stsknutí Enteru se zastaví.
    def show_results(self, screen):
        if not self.end:
            self.total_time = time.time() - self.time_start

            # Výpočet přesnosti: (správný počet znaků) * 100 / (celkovým počtem znaků)
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.word) * 100

            # Výpočet slov za minutu (WPM): průměrně se slovo skládá z 5 písmen, takže vydělíme celkový počet slov pěti 
            # a výsledek vydělíme celkovým časem.
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Čas: ' + str(round(self.total_time)) + "sekund   Přesnost: " + str(
                round(self.accuracy)) + "%" + '   WPM: ' + str(round(self.wpm))

            # obrázek tlačítka
            self.time_img = pygame.image.load('button.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
         
            screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))

            print(self.results)
            pygame.display.update()

    # Hlavní metoda
    def run(self):
        self.reset_game()   # Restart všech proměnných

        self.running = True
        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            # aktualizace textu vloženého uživatelem
            self.draw_text(self.screen, self.input_text, 274, 26, (0, 255, 170))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.display.quit()
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # umístění psacího pole
                    if 100 <= x <= 650 and 250 <= y <= 300:
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                        # Umístění tlačítka
                    if 310 <= x <= 510 and y >= 400 and self.end:
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()

                # Zobrazení výsledků po stisknutí tlačítka Enter a vymazání posledního znaku díky Backspace
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                            self.end = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(60)

    # Umožňí spustit prgram znovu 
    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))

        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.end = False

        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Načtení nové věty
        self.word = self.get_sentence()
        if not self.word: self.reset_game()
        # vykreslení okna
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        msg = "TEST RYCHLOSTI PSANÍ"
        self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)
        # obdélník, kam píšeme text
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        # psaní věty
        self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)

        pygame.display.update()

        

Game().run()
