class Huone:

    def __init__(self, nimi):
        self.nimi = nimi
        self.esineet = []

    def lisää_esine(self, esine):
        self.esineet.append(esine)

    def näytä_esineet(self):
        if len(self.esineet) == 0:
            print("Tässä paikassa ei ole esineitä.")
        else:
            print(f"\n--- {self.nimi.upper()} ---")
            print("Täällä on:")

            for numero, esine in enumerate(self.esineet, 1):
                print(f"{numero}. {esine.nimi}")

    def poimi_esine(self, numero):
        if numero < 1 or numero > len(self.esineet):
            print("Virheellinen esineen numero.")
            return None

        esine = self.esineet.pop(numero - 1)
        
        return esine