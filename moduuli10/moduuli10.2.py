class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f'Hissi on kerroksessa {self.kerros}')

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f'Hissi on kerroksessa {self.kerros}')

    def siirry_kerrokseen(self, kohdekerros):
        while self.kerros < kohdekerros:
            self.kerros_ylös()
        while self.kerros > kohdekerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissit):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(0, hissit):
            h = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(h)

    def aja_hissiä(self, hissin_numero, hissin_kohdekerros):
        self.hissit[hissin_numero - 1].siirry_kerrokseen(hissin_kohdekerros)

t = Talo(1, 6, 4)
t.aja_hissiä(4, 3)