class Auto:

    def __init__(self, rekkari, huippunopeus, nopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = 0

    def kulje(self, tuntimaara):
        self.kuljettumatka += tuntimaara * self.nopeus


class Sahkoauto(Auto):

    def __init__(self, rekkari, huippunopeus, nopeus, akkukapasiteetti_kWh):
        self.akkukapasiteetti_kWh = akkukapasiteetti_kWh
        super().__init__(rekkari, huippunopeus, nopeus)

    def tulosta_tiedot(self):
        print(f'Sähköauton tiedot:\nRekisteritunnus: {self.rekkari}\nHuippunopeus: {self.huippunopeus} km/h'
              f'\nAkun kapasiteetti: {self.akkukapasiteetti_kWh} kWh\nMittarilukema: {self.kuljettumatka} km')

class Polttomoottoriauto(Auto):

    def __init__(self, rekkari, huippunopeus, nopeus, bensatankinkoko_l):
        self.bensatankinkoko_l = bensatankinkoko_l
        super().__init__(rekkari, huippunopeus, nopeus)

    def tulosta_tiedot(self):
        print(f'Polttomoottoriauton tiedot:\nRekisteritunnus: {self.rekkari}\nHuippunopeus: {self.huippunopeus} km/h'
              f'\nBensatankin koko: {self.bensatankinkoko_l} l\nMittarilukema: {self.kuljettumatka} km')

s_auto = Sahkoauto('ABC-15', 180, 140, 52.5)
s_auto.kulje(3)
s_auto.tulosta_tiedot()

print('\n')

pm_auto = Polttomoottoriauto('ACD-123', 165, 125, 32.3)
pm_auto.kulje(3)
pm_auto.tulosta_tiedot()