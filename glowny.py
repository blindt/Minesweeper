
import pygame
from grafika import Kwadrat, Ikony, Ekran
from logika import Plansza
from wyjatki import Wyjatki



class Zarzadca():

    _zwyciestwo = False
    _aktywne = 0
    _poczatek = False
    _przegrana = False
    _lliczba_bomb = 1
    _gliczba_bomb = 1

    def __init__(self, g_szerokosc, g_wysokosc, g_lbomb):
        self._plansza_logiczna = Plansza(g_wysokosc, g_szerokosc, g_lbomb)
        self._plansza_graficzna = [[Kwadrat(i, j, '', (0, 100, 100)) for j in range(15)] for i in range(15)]  # list comprehension
        self._szerokosc = g_szerokosc
        self._wysokosc = g_wysokosc
        self._lbomb = g_lbomb
        Zarzadca._lliczba_bomb = g_lbomb
        Zarzadca._gliczba_bomb = g_lbomb
        self._obiekt_ekranu = Ekran(550, 500, "saper", (120, 200, 200))
        self._ekran = self._obiekt_ekranu.stworz_ekran()
        Ikony.okno_danych(self._ekran, 0)
        Ikony.okno_start(self._ekran, (20, 100, 240))
        Ikony.licznik_bomb(self._ekran, str(self._lbomb))
        self._trzymaj = 0

    def tworz_plansze_logiczna(self):
        for i in range(self._wysokosc):
            for j in range(self._szerokosc):
                if self._plansza_graficzna[i][j].rysuj(self._ekran) == 1:
                    self._plansza_logiczna.losuj(self._lbomb, i, j)
                    self._plansza_logiczna.daj_liczby()
                    'self._plansza_logiczna.wypisz()'
                    self.klikniety(i, j)
                    Zarzadca._poczatek = True
                    self.rysuj()


    def rysuj(self):
        if Zarzadca._zwyciestwo == False and Zarzadca._przegrana == False:
            for i in range(self._wysokosc):
                for j in range(self._szerokosc):
                    if self._trzymaj == 0:
                        if self._plansza_graficzna[i][j].rysuj(self._ekran) == 1:
                            self.klikniety(i, j)
                        elif self._plansza_graficzna[i][j].rysuj(self._ekran) == 2:
                            self._plansza_graficzna[i][j].zaznacz(self._ekran)
                            self._trzymaj = 1
                            self.bomby(i, j)
                        self.wygrana()

                    else:
                        klik = pygame.mouse.get_pressed()
                        if klik[2] == False:
                            self._trzymaj = 0
        elif Zarzadca._przegrana == False:
            Ikony.okno_wygranej(self._ekran)

        Ikony.okno_danych(self._ekran, Ikony.aktywnosc())

        if Ikony.aktywnosc() == 1:
            Ikony.okno_start(self._ekran, (20, 150, 100))
            if pygame.mouse.get_pressed() == (1, 0, 0) and self._aktywne > 0:
                try:
                    if Ikony._nowa_liczba_bomb < 1 or Ikony._nowa_liczba_bomb > (Ikony._nowa_wysokosc*Ikony._nowa_szerokosc)-1:
                        raise Wyjatki
                except Wyjatki:
                    pass
                else:
                    self.od_nowa()
        else:
            Ikony.okno_start(self._ekran, (100, 150, 100))

    def bomby(self, i, j):
        if self._plansza_graficzna[i][j]._poz_zaznaczenia == 2:
            Zarzadca._gliczba_bomb += 1
            if self._plansza_logiczna._tab[i][j] == 'b':
                Zarzadca._lliczba_bomb += 1
        elif self._plansza_graficzna[i][j]._poz_zaznaczenia == 1:
            Zarzadca._gliczba_bomb -= 1
            if self._plansza_logiczna._tab[i][j] == 'b':
                Zarzadca._lliczba_bomb -= 1
        Ikony.licznik_bomb(self._ekran, str(Zarzadca._gliczba_bomb))

    def wygrana(self):
        if Zarzadca._lliczba_bomb == 0 and Zarzadca._gliczba_bomb == 0:
            Zarzadca._zwyciestwo = True
        if self._aktywne == (self._szerokosc*self._wysokosc)-self._lbomb:
            Zarzadca._zwyciestwo = True

    def klikniety(self, i, j):
        if self._plansza_graficzna[i][j]._aktywny == False and self._plansza_graficzna[i][j]._poz_zaznaczenia == 0:
            wsp = self._plansza_logiczna.funkcja(i, j)
            self._aktywne = self._plansza_graficzna[wsp[0]][wsp[1]].aktywny(self._plansza_logiczna._tab[wsp[0]][wsp[1]], self._ekran)
            if wsp[2] == 'b':
                Zarzadca._przegrana = True
            if wsp[2] == 1:
                dd = 1
                de = 1
                ud = -1
                ue = -1
                if i == 0:
                    ud = 0
                elif i == self._wysokosc-1:
                    dd = 0
                if j == 0:
                    ue = 0
                elif j == self._szerokosc-1:
                    de = 0
                return self.klikniety(i+ud, j+ue), self.klikniety(i+ud, j), self.klikniety(i+ud, j+de),\
                       self.klikniety(i, j+ue), self.klikniety(i, j+de), self.klikniety(i+dd, j+ue), \
                       self.klikniety(i+dd, j), self.klikniety(i+dd, j+de)

    def porazka(self):
        Ikony.okno_porazki(self._ekran)

    def od_nowa(self):
        Zarzadca._zwyciestwo = False
        Kwadrat._liczba_aktywnych = 0
        Zarzadca._przegrana = False
        self._szerokosc = Ikony._nowa_szerokosc
        self._wysokosc = Ikony._nowa_wysokosc
        self._lbomb = Ikony._nowa_liczba_bomb
        self._plansza_logiczna = Plansza(self._wysokosc, self._szerokosc, self._lbomb)
        Zarzadca._gliczba_bomb = self._lbomb
        Zarzadca._lliczba_bomb = self._lbomb
        self._aktywne = 0
        pygame.draw.rect(self._ekran, (120, 200, 200), (50, 50, 370, 500), 0)
        for i in range(self._wysokosc):
            for j in range(self._szerokosc):
                self._plansza_graficzna[i][j]._aktywny = False
                self._plansza_graficzna[i][j].ustaw_tekst('')
                self._plansza_graficzna[i][j]._poz_zaznaczenia = 0
                self._plansza_logiczna._tab[i][j] = 0
        Ikony.licznik_bomb(self._ekran, str(self._lbomb))
        Ikony.okno_danych(self._ekran, 0)
        Zarzadca._poczatek = False
        self.tworz_plansze_logiczna()
        self.rysuj()

szerokosc = 15
wysokosc = 15
lbomb = 30
z1 = Zarzadca(szerokosc, wysokosc, lbomb)

'''for i in range(wysokosc):
    for j in range(szerokosc):
        if p1._tab[i][j] == 'b':
            tab[i][j].ustaw('b', (200, 100, 100))
        elif p1._tab[i][j] != '0':
            tab[i][j].ustaw(p1._tab[i][j], (0, 100, 100))
        else:
            tab[i][j].ustaw('', (0, 100, 100))'''


running = True
while running:
    pygame.display.flip()
    if Zarzadca._poczatek == False:
        z1.tworz_plansze_logiczna()
    else:
        z1.rysuj()
    if Zarzadca._przegrana == True:
        z1.porazka()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
