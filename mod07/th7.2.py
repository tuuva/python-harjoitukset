import random


def nopanheitto(tahkot):
    heitto = random.randint(1,tahkot)
    return heitto

maksimi = int(input("Maksimisilmäluku: "))

while True:
    tulos = nopanheitto(maksimi)
    print(tulos)
    if tulos == maksimi:
        break
