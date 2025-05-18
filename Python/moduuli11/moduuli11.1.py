class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f'Kirjan nimi: {self.nimi}\nKirjailija: {self.kirjailija}\nSivumäärä: {self.sivumaara}')

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f'Lehden nimi: {self.nimi}\nLehden päätoimittaja: {self.paatoimittaja}')

k = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
k.tulosta_tiedot()

print('\n')

l = Lehti('Aku Ankka', 'Aki Hyyppä')
l.tulosta_tiedot()