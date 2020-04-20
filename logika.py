from random import seed, randint

class Plansza:


    def __init__(self, x, y, bomby):
        self._x: int = x
        self._y: int = y
        self._tab = [[0 for j in range(y)] for i in range(x)]  # list comprehension

    def funkcja(self, i, j):
        if self._tab[i][j] == 'b':
            return i, j, 'b'
        elif self._tab[i][j] != '0':
            return i, j, 0
        if self._tab[i][j] == '0':
            return i, j, 1

    def wypisz(self):
        for i in range(self._x):
            for j in range(self._y):
                print(self._tab[i][j], end=' ')
            print(' ')

    def losuj(self, bomby, x0, y0):
            seed()
            modyfikatoryy = []
            it = 0
            err = 0
            modyfikatoryx = []
            liczbyx = [randint(0, self._x) for i in range(bomby)]
            liczbyy = [randint(0, self._y) for i in range(bomby)]
            przypadek = [randint(0, 1) for i in range(bomby)]
            for i in range(bomby):
                if przypadek[i] == 1:
                    modyfikatoryy.append(randint(-1*self._y, self._y))
                    modyfikatoryx.append(1)
                else:
                    modyfikatoryy.append(1)
                    modyfikatoryx.append(randint(-1*self._x, self._x))
            wynikx = [(i + j) % self._x for i, j in zip(liczbyx, modyfikatoryx)]
            wyniky = [(i + j) % self._y for i, j in zip(liczbyy, modyfikatoryy)]
            for i in range(bomby):
                    if self._tab[wynikx[it]][wyniky[it]] == 'b':
                        err += 1
                    elif wynikx[it] == x0 and wyniky[it] == y0:
                        err += 1
                    else:
                        self._tab[wynikx[it]][wyniky[it]] = 'b'
                    it += 1
            if err > 0:
                return self.losuj(err, x0, y0)

    def daj_liczby(self):
        for i in range(self._x):
            for j in range(self._y):
                if self._tab[i][j] != 'b':
                    mi = -1
                    mj = -1
                    di = 2
                    dj = 2
                    c = 0
                    if i == 0:
                        mi = 0
                    elif i == self._x-1:
                        di = 1
                    if j == 0:
                        mj = 0
                    elif j == self._y-1:
                        dj = 1
                    for ii in range(mi, di):
                        for jj in range(mj, dj):
                            if self._tab[ii+i][jj+j] == 'b':
                                c += 1
                    self._tab[i][j] = str(c)