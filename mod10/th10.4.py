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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka")
        print("")

        for auto in self.autot:
            print(
                auto.rekisteritunnus,
                "|",
                auto.huippunopeus,
                "|",
                auto.tämänhetkinen_nopeus,
                "|",
                auto.kuljettu_matka
            )

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True

        return False

autot = []

for i in range(10):
    rekisteritunnus = "ABC-" + str(i + 1)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)


tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

print()
print("Kilpailu on päättynyt!")
kilpailu.tulosta_tilanne()