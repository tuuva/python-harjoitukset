
class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.ajettu_aika = 3 
        self.matkamittari = 0
        
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        print("")
        print(f"Sähköauton rekisteritunnus: {self.rekisteritunnus}, huippunopeus: {self.huippunopeus} km/h, akkukapasiteetti: {self.akkukapasiteetti} kWh")
        print("")
        print(f"auton tämänhetkinen nopeus: {self.tämänhetkinen_nopeus} kmh")
        print("")
        print(f"matramittarin lukema: {self.matkamittari} km")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def tulosta_tiedot(self):
        print("")
        print("")
        print(f"Polttomoottoriauton rekisteritunnus: {self.rekisteritunnus}, bensatankin koko: {self.bensatankin_koko} litraa, huippunopeus: {self.huippunopeus} km/h")
        print("")
        print(f"auton tämänhetkinen nopeus: {self.tämänhetkinen_nopeus} km/h")
        print("")
        print(f"matkamittarin lukema: {self.matkamittari} km")

auto1 = Sähköauto("ABC-15", 180, 52.5)
auto1.tämänhetkinen_nopeus = 60
auto1.matkamittari = auto1.tämänhetkinen_nopeus * auto1.ajettu_aika

auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)
auto2.tämänhetkinen_nopeus = 70
auto2.matkamittari = auto2.tämänhetkinen_nopeus * auto2.ajettu_aika

auto1.tulosta_tiedot()
auto2.tulosta_tiedot()