from pelaaja import Pelaaja
from esine import Esine
from huone import Huone


def luo_peli():

    lyhty = Esine("Lyhty", 1.5)
    taikajuoma = Esine("Taikajuoma", 0.5)
    avain = Esine("Avain", 0.1)

    alkuhuone = Huone("Alkuhuone")
    metsä = Huone("Metsä")
    luola = Huone("Luola")

    alkuhuone.lisää_esine(lyhty)
    alkuhuone.lisää_esine(taikajuoma)
    alkuhuone.lisää_esine(avain)

    nimi = input("Mikä on nimesi?: ")

    pelaaja = Pelaaja(nimi, alkuhuone)

    return pelaaja, metsä, luola


def valikko():

    print("\n--- VALIKKO ---")
    print("1. Tutki huonetta")
    print("2. Kerää esine")
    print("3. Liiku")
    print("4. Näytä omat esineet")
    print("5. Lopeta")


def pelaa():

    pelaaja, metsä, luola = luo_peli()

    print()
    print(f"Tervetuloa peliin, {pelaaja.nimi}!")
    print(f"Olet huoneessa: {pelaaja.sijainti.nimi}")

    while True:

        valikko()

        valinta = input("Valitse toiminto: ")

        if valinta == "1":

            pelaaja.sijainti.näytä_esineet()

        elif valinta == "2":

            if len(pelaaja.sijainti.esineet) == 0:

                print("Huoneessa ei ole esineitä.")

            else:

                pelaaja.sijainti.näytä_esineet()

                valinta = input("Minkä esineen haluat ottaa? ")

                if valinta.isdigit():

                    numero = int(valinta) - 1

                    if 0 <= numero < len(pelaaja.sijainti.esineet):

                        esine = pelaaja.sijainti.esineet.pop(numero)

                        pelaaja.kerää_esine(esine)

                    else:

                        print("Tuolla numerolla ei ole esinettä.")

                else:

                    print("Anna numero.")

        elif valinta == "3":

            print("\nMinne haluat mennä?")
            print("1. Metsä")
            print("2. Luola")
            print("3. Peruuta")

            kohde = input("Valitse: ")

            if kohde == "1":

                pelaaja.liiku(metsä)

            elif kohde == "2":

                pelaaja.liiku(luola)

            elif kohde == "3":

                print("Et liiku mihinkään.")

            else:

                print("Virheellinen valinta.")

        elif valinta == "4":

            pelaaja.näytä_esineet()

        elif valinta == "5":

            print("Peli lopetetaan.")
            break

        else:

            print("Virheellinen valinta.")


pelaa()