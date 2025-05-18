class Auto:
    def __init__ (self, rekkari, maxnopeus):
        self.rekkari = rekkari
        self.maxnopeus = maxnopeus
        self.nytnopeus = 0
        self.matka = 0

auto1 = Auto("ABC-123", 142)
print(f'Auton rekisteritunnus: {auto1.rekkari}\nHuippunopeus: {auto1.maxnopeus} km/h'
      f'\nTämänhekinen nopeus: {auto1.nytnopeus} \nKuljettu matka: {auto1.matka}')
