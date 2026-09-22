class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return

class Hoitola:
    def __init__(self):
        self.koirat = []
    def koira_sisään(self,koira):
        self.koirat.append(koira)
    def koira_ulos(self,koira):
        self.koirat.remove(koira)
    def tervehdi_koira(self):
        for koira in self.koirat:
            koira.hauku(1)

koira1 = Koira("Max", 2020)
koira2 = Koira("Rekku", 2022, "Viu viu")
hoitola = Hoitola()

hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)
hoitola.tervehdi_koira()

                