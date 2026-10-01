class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.esineet = []

    def lisää_esine(self, esine):
        self.esineet.append(esine)

    def näytä_esineet(self):
        if len(self.esineet) == 0:
            print("Huoneessa ei ole esineitä.")
        else:
            print(f"\nHuoneessa {self.nimi} on:")

            for numero, esine in enumerate(self.esineet, 1):
                print(f"{numero}. {esine}")