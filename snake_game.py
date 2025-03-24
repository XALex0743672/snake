import pygame
import random
import os
import sys

# Helper function to handle resource paths when packaged with PyInstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()

szerokosc, wysokosc = 800, 600
okno = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Snake")

bialy = (255, 255, 255)
zielony = (0, 255, 0)
czerwony = (255, 0, 0)
czarny = (0, 0, 0)
zolty = (255, 255, 0)
niebieski = (0, 0, 255)

rozmiar_bloku = 20
predkosc_podstawowa = 15

# Use default font if custom font file is not available
try:
    font = pygame.font.SysFont(None, 40)
except:
    font = pygame.font.Font(None, 40)

def wyswietl_tekst(tekst, kolor, x, y):
    wiadomosc = font.render(tekst, True, kolor)
    okno.blit(wiadomosc, [x, y])

def ekran_koncowy(punkty):
    okno.fill(czarny)
    wyswietl_tekst(f"Koniec gry! Wynik: {punkty}", bialy, szerokosc // 4, wysokosc // 3)
    wyswietl_tekst("Naciśnij 'R', aby zagrać ponownie", bialy, szerokosc // 4, wysokosc // 2)
    pygame.display.update()
    czekaj = True
    while czekaj:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                exit()
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_r:
                    gra()

def wybierz_trudnosc():
    okno.fill(czarny)
    wyswietl_tekst("Wybierz poziom trudności:", bialy, szerokosc // 4, wysokosc // 3)
    wyswietl_tekst("1 - Łatwy | 2 - Średni | 3 - Trudny", bialy, szerokosc // 4, wysokosc // 2)
    pygame.display.update()
    while True:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                exit()
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_1:
                    return 10
                elif zdarzenie.key == pygame.K_2:
                    return 15
                elif zdarzenie.key == pygame.K_3:
                    return 20

def gra():
    predkosc = wybierz_trudnosc()
    zegar = pygame.time.Clock()
    x, y = szerokosc // 2, wysokosc // 2
    x_zmiana, y_zmiana = 0, 0

    cialo = [(x, y)]
    dlugosc = 1

    punkt_x = random.randrange(0, szerokosc - rozmiar_bloku, rozmiar_bloku)
    punkt_y = random.randrange(0, wysokosc - rozmiar_bloku, rozmiar_bloku)

    bomba_x = random.randrange(0, szerokosc - rozmiar_bloku, rozmiar_bloku)
    bomba_y = random.randrange(0, wysokosc - rozmiar_bloku, rozmiar_bloku)

    bonus_x = bonus_y = -1
    bonus_czas = 0

    punkty = 0
    dziala = True

    while dziala:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_LEFT and x_zmiana == 0:
                    x_zmiana, y_zmiana = -rozmiar_bloku, 0
                elif zdarzenie.key == pygame.K_RIGHT and x_zmiana == 0:
                    x_zmiana, y_zmiana = rozmiar_bloku, 0
                elif zdarzenie.key == pygame.K_UP and y_zmiana == 0:
                    x_zmiana, y_zmiana = 0, -rozmiar_bloku
                elif zdarzenie.key == pygame.K_DOWN and y_zmiana == 0:
                    x_zmiana, y_zmiana = 0, rozmiar_bloku

        x += x_zmiana
        y += y_zmiana

        if x < 0 or x >= szerokosc or y < 0 or y >= wysokosc:
            ekran_koncowy(punkty)

        cialo.append((x, y))
        if len(cialo) > dlugosc:
            cialo.pop(0)

        if len(cialo) != len(set(cialo)):
            ekran_koncowy(punkty)

        if (x, y) == (punkt_x, punkt_y):
            punkty += 1
            dlugosc += 1
            punkt_x = random.randrange(0, szerokosc - rozmiar_bloku, rozmiar_bloku)
            punkt_y = random.randrange(0, wysokosc - rozmiar_bloku, rozmiar_bloku)

            bomba_x = random.randrange(0, szerokosc - rozmiar_bloku, rozmiar_bloku)
            bomba_y = random.randrange(0, wysokosc - rozmiar_bloku, rozmiar_bloku)

            if punkty % 5 == 0:
                bonus_x = random.randrange(0, szerokosc - rozmiar_bloku, rozmiar_bloku)
                bonus_y = random.randrange(0, wysokosc - rozmiar_bloku, rozmiar_bloku)
                bonus_czas = 100

            if punkty % 10 == 0:
                predkosc += 1

        if (x, y) == (bomba_x, bomba_y):
            ekran_koncowy(punkty)

        if (x, y) == (bonus_x, bonus_y):
            punkty += 5
            bonus_x = bonus_y = -1

        okno.fill(czarny)
        wyswietl_tekst(f"Punkty: {punkty}", bialy, 10, 10)

        pygame.draw.rect(okno, zielony, (punkt_x, punkt_y, rozmiar_bloku, rozmiar_bloku))

        if pygame.time.get_ticks() // 300 % 2 == 0:
            pygame.draw.rect(okno, czerwony, (bomba_x, bomba_y, rozmiar_bloku, rozmiar_bloku))
        else:
            pygame.draw.rect(okno, niebieski, (bomba_x, bomba_y, rozmiar_bloku, rozmiar_bloku))

        if bonus_czas > 0:
            pygame.draw.rect(okno, zolty, (bonus_x, bonus_y, rozmiar_bloku, rozmiar_bloku))
            bonus_czas -= 1

        for segment in cialo:
            pygame.draw.rect(okno, bialy, (segment[0], segment[1], rozmiar_bloku, rozmiar_bloku))

        pygame.display.update()
        zegar.tick(predkosc)

# Main game entry point
if __name__ == "__main__":
    try:
        gra()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)
