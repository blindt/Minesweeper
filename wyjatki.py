import pygame
import time

pygame.init()

BLACK = (0,0,0)

def ustaw_tekst(tekst, typ_czcionki):
    czcionka = typ_czcionki.render(tekst, True, BLACK)
    return czcionka, czcionka.get_rect()


moja_czcionkao = pygame.font.Font('freesansbold.ttf', 15)

pygame.init()

class Wyjatki(Exception):

    def __init__(self):
        pass
    def zly_wymiar(self, ekran, y,x):
        moja_czcionkao = pygame.font.Font('freesansbold.ttf', 12)
        czcionka, tekst_kwadrat = ustaw_tekst("zle dane:", moja_czcionkao)
        tekst_kwadrat.center = (y + 80, x)
        ekran.blit(czcionka, tekst_kwadrat)