import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tunnit):
        uusi_matka = self.tämänhetkinen_nopeus * tunnit
        self.kuljettu_matka += uusi_matka


autot = []

for i in range(10):
    rekisteritunnus = "ABC-" + str(i + 1)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)

        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break


print()
print("Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka")
print("")

for auto in autot:
    print(
        auto.rekisteritunnus,
        "|",
        auto.huippunopeus,
        "|",
        auto.tämänhetkinen_nopeus,
        "|",
        auto.kuljettu_matka
    )