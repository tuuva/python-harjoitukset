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

       
auto = Auto("ABC-123", 142)

print("rekisteritunnus:", auto.rekisteritunnus)
print("huippunopeus:", auto.huippunopeus, "km/h")
print("tämänhetkinen nopeus:", auto.tämänhetkinen_nopeus, "km/h")
print("kuljettu matka:", auto.kuljettu_matka, "km")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print("Nopeus kiihdytysten jälkeen:", auto.tämänhetkinen_nopeus, "km/h")

auto.kiihdytä(-200)

print("Nopeus hätäjarrutuksen jälkeen:", auto.tämänhetkinen_nopeus, "km/h")