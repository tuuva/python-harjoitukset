
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto= Auto("ABC-123", 142)

print("rekisteritunnus:", auto.rekisteritunnus)
print("huippunopeus:", auto.huippunopeus, "km/h")
print("tämänhetkinen nopeus:", auto.tämänhetkinen_nopeus, "km/h")
print("kuljettu matka:", auto.kuljettu_matka, "km")
