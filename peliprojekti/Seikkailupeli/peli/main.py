from pelaaja import Pelaaja
from esine import Esine
from huone import Huone
import json


def luo_peli():

    # Esineet
    radiopuhelin = Esine("Radiopuhelin")
    kartta = Esine("Kartta")
    taskulamppu = Esine("Taskulamppu")
    kompassi = Esine("Kompassi")

    # Paikat
    lentokentta = Huone("Lentokenttä")
    mokki = Huone("Tutkijan mökki")
    laboratorio = Huone("Laboratorio")
    majakka = Huone("Majakka")

    # Esineet lentokentälle
    lentokentta.lisää_esine(radiopuhelin)
    lentokentta.lisää_esine(kartta)
    lentokentta.lisää_esine(taskulamppu)
    lentokentta.lisää_esine(kompassi)

    nimi = input("Mikä on nimesi?: ")

    pelaaja = Pelaaja(nimi, lentokentta)

    return pelaaja, mokki, laboratorio, majakka


def valikko():

    print("\n--- VALIKKO ---")
    print("1. Tutki paikkaa")
    print("2. Liiku")
    print("3. Näytä omat esineet")
    print("4. Tallenna peli")
    print("5. Lopeta")


def tallenna_peli(pelaaja):

    tallennus = {
        "nimi": pelaaja.nimi,
        "sijainti": pelaaja.sijainti.nimi,
        "esineet": []
    }

    for esine in pelaaja.esineet:
        tallennus["esineet"].append(esine.nimi)

    try:
        with open("save.json", "w", encoding="utf-8") as tiedosto:
            json.dump(
                tallennus,
                tiedosto,
                ensure_ascii=False,
                indent=4
            )

        print("Peli tallennettu.")

    except IOError:
        print("Pelin tallentaminen epäonnistui.")


def ota_esine(pelaaja):

    huone = pelaaja.sijainti

    if len(huone.esineet) == 0:
        print("Täällä ei ole esineitä.")
        return

    huone.näytä_esineet()

    try:
        valinta = int(input("Minkä esineen haluat ottaa? "))

        esine = huone.poimi_esine(valinta)

        if esine is not None:
            pelaaja.kerää_esine(esine)

    except ValueError:
        print("Anna numero.")


def liiku(pelaaja, mokki, laboratorio, majakka):

    print("\n--- MINNE HALUAT MENNÄ? ---")
    print("1. Tutkijan mökki")
    print("2. Laboratorio")
    print("3. Majakka")
    print("4. Peruuta")

    valinta = input("Valitse: ")

    if valinta == "1":
        pelaaja.liiku(mokki)

    elif valinta == "2":
        pelaaja.liiku(laboratorio)

    elif valinta == "3":
        pelaaja.liiku(majakka)

    elif valinta == "4":
        print("Et liiku mihinkään.")

    else:
        print("Virheellinen valinta.")


def pelaa():

    pelaaja, mokki, laboratorio, majakka = luo_peli()

    print(f"\nTervetuloa peliin, {pelaaja.nimi}!")
    print(f"Olet paikassa: {pelaaja.sijainti.nimi}")

    while True:

        valikko()

        valinta = input("Valitse toiminto: ")

        if valinta == "1":

            pelaaja.sijainti.näytä_esineet()

            if len(pelaaja.sijainti.esineet) > 0:

                vastaus = input(
                    "Haluatko ottaa jonkin esineen? (k/e): "
                )

                if vastaus.lower() == "k":
                    ota_esine(pelaaja)

        elif valinta == "2":

            liiku(
                pelaaja,
                mokki,
                laboratorio,
                majakka
            )

        elif valinta == "3":

            pelaaja.näytä_esineet()

        elif valinta == "4":

            tallenna_peli(pelaaja)

        elif valinta == "5":

            print("Peli lopetetaan.")
            break

        else:

            print("Virheellinen valinta.")


pelaa()