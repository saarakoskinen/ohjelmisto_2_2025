import random

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

    def kulje (self, h):
        self.matka += h * self.nopeus

if __name__ == '__main__':
    autot = []
    for i in range(10):
        rekkari = f'ABC-{i +1}'
        maxnopeus = random.randint(100, 200)
        autot.append(Auto(rekkari, maxnopeus))

kilpailu = True
while kilpailu:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu = False
            break

print(f"{'Rekisteri':<10}{'Huippunopeuss':<10}{'Matka (km)':<10}")
for auto in autot:
    print(f"{auto.rekkari:<10}{auto.maxnopeus:<10}{auto.matka:<10.0f}")