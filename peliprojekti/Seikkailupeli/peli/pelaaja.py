class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def kerää_esine(self, esine):
        self.esineet.append(esine)
        print(f"Keräsit esineen: {esine.nimi}")

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Siirryit huoneeseen: {huone.nimi}")

    def näytä_esineet(self):
        print("\nMukanasi olevat esineet:")

        if len(self.esineet) == 0:
            print("- Ei esineitä")
        else:
            for esine in self.esineet:
                print(f"- {esine}")
