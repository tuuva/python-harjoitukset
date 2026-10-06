class Pelaaja:

    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.esineet = []

    def kerää_esine(self, esine):
        self.esineet.append(esine)
        print(f"Keräsit esineen: {esine.nimi}")

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Siirryit paikkaan: {huone.nimi}")

    def näytä_esineet(self):
        print("\n--- MUKANASI OLEVAT ESINEET ---")

        if len(self.esineet) == 0:
            print("Sinulla ei ole esineitä.")
        else:
            for numero, esine in enumerate(self.esineet, 1):
                print(f"{numero}. {esine.nimi}")

    def onko_esine(self, esineen_nimi):
        for esine in self.esineet:
            if esine.nimi.lower() == esineen_nimi.lower():
                return True

        return False
