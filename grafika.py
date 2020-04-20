import pygame
import inputbox
from wyjatki import Wyjatki

pygame.init()


BLACK = (0, 0, 0)

def ustaw_tekst(tekst, typ_czcionki):
    czcionka = typ_czcionki.render(tekst, True, BLACK)
    return czcionka, czcionka.get_rect()


moja_czcionka = pygame.font.Font('freesansbold.ttf', 20)
moja_czcionkaporazkazwyciestwo = pygame.font.Font('freesansbold.ttf', 25)

class Ekran:
    def __init__(self, e_szerokosc, e_wysokosc, tytul, kolor):
        self._szerokosc = e_szerokosc
        self._wysokosc = e_wysokosc
        self._kolor = kolor
        self._tytul = tytul

    def stworz_ekran(self):
        pygame.display.set_caption(self._tytul)
        self._ekran = pygame.display.set_mode((self._szerokosc, self._wysokosc))
        self._ekran.fill(self._kolor)
        return self._ekran

class Kwadrat:
    _szerokosc = 20
    _wysokosc = 20
    _ostatnix = 0
    _ostatniy = 0
    _ostatnii = 0
    _ostatnij = 0
    _liczba_aktywnych = 0

    def __init__(self, x, y, tekst, kolor):
        self._x = (x*Kwadrat._szerokosc+80)+2*x
        self._y = (y*Kwadrat._wysokosc+80)+2*y
        self._i = x
        self._j = y
        _ostatnii = x
        _ostatnij = y
        self._tekst = tekst
        self._kolor = kolor
        self._aktywny = False
        Kwadrat._ostatnix = self._x
        Kwadrat._ostatniy = self._y
        self._poz_zaznaczenia = 0


    @staticmethod
    def ustaw_ostatnie_wspolrzedne(x, y):
        Kwadrat._ostatniy = y
        Kwadrat._ostatnix = x

    def rysuj(self, window):
        (x, y) = pygame.mouse.get_pos()
        if self._aktywny == False:
            if y >= self._x and y <= self._x + Kwadrat._wysokosc and x >= self._y and x <= self._y + Kwadrat._szerokosc:
                self._kolor = (150, 200, 100)
                klik=pygame.mouse.get_pressed()
                if klik[0] == True:
                    return 1
                if klik[2] == True:
                    return 2

            else:
                self._kolor = (0, 100, 100)
            pygame.draw.rect(window, self._kolor, (self._y, self._x, Kwadrat._szerokosc, Kwadrat._wysokosc), 0)
            czcionka, tekst_kwadrat = ustaw_tekst(self._tekst, moja_czcionka)
            tekst_kwadrat.center = ((self._y + Kwadrat._wysokosc / 2), (self._x + Kwadrat._szerokosc / 2))
            window.blit(czcionka, tekst_kwadrat)

    def ustaw_tekst(self, tekst):
        self._tekst = tekst

    def aktywny(self, wartosc, window):
        self._kolor = (230, 150, 50)
        self._aktywny = True
        pygame.draw.rect(window, self._kolor, (self._y, self._x, Kwadrat._szerokosc, Kwadrat._wysokosc), 0)
        if wartosc != '0':
            self._tekst = wartosc
            pygame.draw.rect(window, self._kolor, (self._y, self._x, Kwadrat._szerokosc, Kwadrat._wysokosc), 0)
            czcionka, tekst_kwadrat = ustaw_tekst(self._tekst, moja_czcionka)
            tekst_kwadrat.center = ((self._y + Kwadrat._wysokosc / 2), (self._x + Kwadrat._szerokosc / 2))
            window.blit(czcionka, tekst_kwadrat)
        Kwadrat._liczba_aktywnych +=1
        return Kwadrat._liczba_aktywnych



    def zaznacz(self, window):

        kw = lambda x, y: x + y/2
        if self._poz_zaznaczenia == 0:
            self._tekst = 'M'
            czcionka, tekst_kwadrat = ustaw_tekst(self._tekst, moja_czcionka)
            tekst_kwadrat.center = (kw(self._y, Kwadrat._wysokosc), kw(self._x, Kwadrat._szerokosc))
            window.blit(czcionka, tekst_kwadrat)
        if self._poz_zaznaczenia == 1:
            self._tekst = '?'
            czcionka, tekst_kwadrat = ustaw_tekst(self._tekst, moja_czcionka)
            tekst_kwadrat.center = (kw(self._y, Kwadrat._wysokosc), kw(self._x, Kwadrat._szerokosc))
            window.blit(czcionka, tekst_kwadrat)
        if self._poz_zaznaczenia == 2:
            self._tekst = ''
            czcionka, tekst_kwadrat = ustaw_tekst(self._tekst, moja_czcionka)
            tekst_kwadrat.center = (kw(self._y, Kwadrat._wysokosc), kw(self._x, Kwadrat._szerokosc))
            window.blit(czcionka, tekst_kwadrat)

        self._poz_zaznaczenia = (self._poz_zaznaczenia+1) % 3


class Ikony(Kwadrat):

    _start = 0
    _nowa_liczba_bomb = 30
    _nowa_szerokosc = 15
    _nowa_wysokosc = 15
    _test = 1

    @staticmethod
    def aktywnosc():
        (x, y) = pygame.mouse.get_pos()
        if y >= 261 and y <= 301 and x >= Kwadrat._ostatniy + 40 and x <= Kwadrat._ostatniy + 120:
            return 1
        if y >= 108 and y <= 132 and x >= Kwadrat._ostatniy + 50 and x <= Kwadrat._ostatniy + 110:
            return 2
        if y >= 163 and y <= 187 and x >= Kwadrat._ostatniy + 50 and x <= Kwadrat._ostatniy + 110:
            return 3
        if y >= 219 and y <= 243 and x >= Kwadrat._ostatniy + 50 and x <= Kwadrat._ostatniy + 110:
            return 4

    @staticmethod
    def okno_porazki(ekran):
        okno = lambda a, b: (a+(2*b)+80)/2
        czcionka, tekst_kwadrat = ustaw_tekst("Porażka", moja_czcionkaporazkazwyciestwo)
        tekst_kwadrat.center = (okno(Kwadrat._ostatniy, Kwadrat._ostatnii),okno(Kwadrat._ostatnix, Kwadrat._ostatnij))
        ekran.blit(czcionka, tekst_kwadrat)

    @staticmethod
    def okno_wygranej(ekran):
        okno = lambda a, b: (a + (2 * b) + 80) / 2
        czcionka, tekst_kwadrat = ustaw_tekst("Zwycięstwo!", moja_czcionkaporazkazwyciestwo)
        tekst_kwadrat.center = (okno(Kwadrat._ostatniy, Kwadrat._ostatnii), okno(Kwadrat._ostatnix, Kwadrat._ostatnij))
        ekran.blit(czcionka, tekst_kwadrat)

    @staticmethod
    def okno_danych(ekran, dane):

        ramka = lambda wys: pygame.draw.rect(ekran, (0, 0, 0), (Kwadrat._ostatniy+40, wys, 80, 40), 0)
        srodek = lambda wys: pygame.draw.rect(ekran, (30, 100, 80), (Kwadrat._ostatniy+50, wys, 60, 24), 0)
        podswietlony = lambda wys: pygame.draw.rect(ekran, (50, 200, 50), (Kwadrat._ostatniy + 50, wys, 60, 24), 0)

        if Ikony._start == 0:
            ramka(100)
            srodek(108)
            moja_czcionkao = pygame.font.Font('freesansbold.ttf', 15)
            czcionka, tekst_kwadrat = ustaw_tekst("Szerokość:", moja_czcionkao)
            tekst_kwadrat.center = (Kwadrat._ostatniy+80, 90)
            ekran.blit(czcionka, tekst_kwadrat)

            ramka(155)
            srodek(163)
            czcionka, tekst_kwadrat = ustaw_tekst("Wysokość:", moja_czcionkao)
            tekst_kwadrat.center = (Kwadrat._ostatniy+80, 148)
            ekran.blit(czcionka, tekst_kwadrat)

            ramka(211)
            srodek(219)
            czcionka, tekst_kwadrat = ustaw_tekst("Liczba bomb:", moja_czcionkao)
            tekst_kwadrat.center = (Kwadrat._ostatniy + 80, 204)
            ekran.blit(czcionka, tekst_kwadrat)
            Ikony._start = 1

        if dane == 2:
            podswietlony(108)
            Ikony._test = 1
            klik = pygame.mouse.get_pressed()
            if klik[0] == True:
                Ikony._nowa_szerokosc = int(inputbox.ask(ekran, Kwadrat._ostatniy + 50, 112))
                try:
                    if Ikony._nowa_szerokosc < 2 or Ikony._nowa_szerokosc > 15:
                        raise Wyjatki
                except Wyjatki as err:
                    srodek(108)
                    Ikony._nowa_szerokosc = 15
                    err.zly_wymiar(ekran, Kwadrat._ostatniy, 116)
                    Ikony._test = 0

        elif Ikony._test == 1:
            srodek(108)

        if dane == 3:
            podswietlony(163)
            Ikony._test = 1
            klik = pygame.mouse.get_pressed()
            if klik[0] == True:
                Ikony._nowa_wysokosc = int(inputbox.ask(ekran, Kwadrat._ostatniy + 50, 167))
                try:
                    if Ikony._nowa_wysokosc < 2 or Ikony._nowa_wysokosc > 15:
                        raise Wyjatki
                except Wyjatki as err:
                    srodek(163)
                    Ikony._nowa_wysokosc = 15
                    err.zly_wymiar(ekran, Kwadrat._ostatniy, 173)
                    Ikony._test = 0

        elif Ikony._test == 1:
            srodek(163)

        if dane == 4:
            podswietlony(219)
            klik = pygame.mouse.get_pressed()
            if klik[0] == True:
                Ikony._nowa_liczba_bomb = int(inputbox.ask(ekran, Kwadrat._ostatniy + 50, 224))
                ramka(211)

        else:
            srodek(219)

    @staticmethod
    def okno_start(ekran, kolor):

        pygame.draw.rect(ekran, kolor, (Kwadrat._ostatniy + 40, 261, 80, 40), 0)
        czcionka, tekst_kwadrat = ustaw_tekst("START", moja_czcionka)
        tekst_kwadrat.center = (Kwadrat._ostatniy + 80, 283)
        ekran.blit(czcionka, tekst_kwadrat)

    @staticmethod
    def licznik_bomb(ekran, liczba):
        pygame.draw.rect(ekran, (0, 0, 0), ((Kwadrat._ostatniy+(2*Kwadrat._ostatnii)+80)/2 ,10, 40, 40), 0)
        pygame.draw.rect(ekran, (10, 200, 10), (((Kwadrat._ostatniy + (2 * Kwadrat._ostatnii) + 80) / 2)+5, 15, 30, 30), 0)
        czcionka, tekst_kwadrat = ustaw_tekst(liczba, moja_czcionka)
        tekst_kwadrat.center = (((Kwadrat._ostatniy+(2*Kwadrat._ostatnii)+80)/2)+20, 30)
        ekran.blit(czcionka, tekst_kwadrat)
