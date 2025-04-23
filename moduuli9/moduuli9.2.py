class Auto:
    def __init__ (self, rekkari, maxnopeus):
        self.rekkari = rekkari
        self.maxnopeus = maxnopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta (self, kmh):
        self.nopeus += kmh
        if self.nopeus > self.maxnopeus:
            self.nopeus = self.maxnopeus
        if self.nopeus < 0:
            self.nopeus = 0



auto1 = Auto("ABC-123", 142)
print(f'Auton rekisteritunnus: {auto1.rekkari}\nHuippunopeus: {auto1.maxnopeus} km/h'
      f'\nTämänhekinen nopeus: {auto1.nopeus} \nKuljettu matka: {auto1.matka}')

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f'\nAuton rekisteritunnus: {auto1.rekkari}\nHuippunopeus: {auto1.maxnopeus} km/h'
      f'\nTämänhekinen nopeus: {auto1.nopeus} \nKuljettu matka: {auto1.matka}')

auto1.kiihdyta(-200)

print(f'\nAuton rekisteritunnus: {auto1.rekkari}\nHuippunopeus: {auto1.maxnopeus} km/h'
      f'\nTämänhekinen nopeus: {auto1.nopeus} \nKuljettu matka: {auto1.matka}')