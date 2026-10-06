from pelaaja import Pelaaja
from esine import Esine
from huone import Huone
import json


def lue_intro():
    try:
        with open("peliprojekti/Seikkailupeli/peli/intro.txt", "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())

    except FileNotFoundError:
        print("Intro-tiedostoa ei löydy.")

    except IOError:
        print("Tiedoston lukemisessa tapahtui virhe.")


def lue_ohjeet():
    try:
        with open("peliprojekti/Seikkailupeli/peli/ohjeet.txt", "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())

    except FileNotFoundError:
        print("Ohjeet-tiedostoa ei löydy.")

    except IOError:
        print("Tiedoston lukemisessa tapahtui virhe.")


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

        print("\nPeli tallennettu.")

    except IOError:
        print("\nPelin tallentaminen epäonnistui.")


def lataa_peli(nimi, lentokentta, mokki, laboratorio, majakka):

    try:
        with open("save.json", "r", encoding="utf-8") as tiedosto:
            tallennus = json.load(tiedosto)

    except FileNotFoundError:
        return None

    except json.JSONDecodeError:
        return None

    if tallennus["nimi"] != nimi:
        return None

    print("\nVanha tallennus löytyi!")

    vastaus = input("Haluatko jatkaa vanhaa peliä? (k/e): ")

    if vastaus.lower() != "k":
        return None

    if tallennus["sijainti"] == "Lentokenttä":
        sijainti = lentokentta

    elif tallennus["sijainti"] == "Tutkijan mökki":
        sijainti = mokki

    elif tallennus["sijainti"] == "Laboratorio":
        sijainti = laboratorio

    elif tallennus["sijainti"] == "Majakka":
        sijainti = majakka

    else:
        sijainti = lentokentta

    pelaaja = Pelaaja(nimi, sijainti)

    for esineen_nimi in tallennus["esineet"]:
        esine = Esine(esineen_nimi)
        pelaaja.kerää_esine(esine)

    return pelaaja


def luo_peli():

    radiopuhelin = Esine("Radiopuhelin")
    kartta = Esine("Kartta")
    taskulamppu = Esine("Taskulamppu")
    kompassi = Esine("Kompassi")

    avain = Esine("Avain")
    paivakirja = Esine("Päiväkirja")
    paristot = Esine("Paristot")

    tutkimusraportti = Esine("Tutkimusraportti")
    sulake = Esine("Sulake")
    laboratorion_avain = Esine("Laboratorion avain")

    radiolaite = Esine("Vanha radiolaite")
    tutkijan_muistiinpano = Esine("Tutkijan muistiinpano")

    lentokentta = Huone("Lentokenttä")
    mokki = Huone("Tutkijan mökki")
    laboratorio = Huone("Laboratorio")
    majakka = Huone("Majakka")

    lentokentta.lisää_esine(radiopuhelin)
    lentokentta.lisää_esine(kartta)
    lentokentta.lisää_esine(taskulamppu)
    lentokentta.lisää_esine(kompassi)

    mokki.lisää_esine(avain)
    mokki.lisää_esine(paivakirja)
    mokki.lisää_esine(paristot)

    laboratorio.lisää_esine(tutkimusraportti)
    laboratorio.lisää_esine(sulake)
    laboratorio.lisää_esine(laboratorion_avain)

    majakka.lisää_esine(radiolaite)
    majakka.lisää_esine(tutkijan_muistiinpano)

    nimi = input("\nMikä on nimesi?: ")

    vanha_peli = lataa_peli(
        nimi,
        lentokentta,
        mokki,
        laboratorio,
        majakka
    )

    if vanha_peli is not None:
        return vanha_peli, mokki, laboratorio, majakka

    pelaaja = Pelaaja(nimi, lentokentta)

    return pelaaja, mokki, laboratorio, majakka


def ota_esine(pelaaja):

    huone = pelaaja.sijainti

    if len(huone.esineet) == 0:
        print("\nTässä paikassa ei ole esineitä.")
        return

    huone.näytä_esineet()

    try:
        valinta = int(input("Minkä esineen haluat ottaa? "))

        esine = huone.poimi_esine(valinta)

        if esine is not None:
            pelaaja.kerää_esine(esine)

    except ValueError:
        print("Anna numero.")


def tutki_esine(esine):

    if esine.nimi == "Radiopuhelin":

        print("\nRadiopuhelin näyttää toimivan.")
        print("Sillä voisi ottaa yhteyttä ulkopuoliseen maailmaan.")

    elif esine.nimi == "Kartta":

        print("\nKartta näyttää saaren tärkeimmät paikat.")
        print("Karttaan on merkitty lentokenttä,")
        print("mökki, laboratorio ja majakka.")

    elif esine.nimi == "Taskulamppu":

        print("\nTaskulamppu toimii.")
        print("Siitä voi olla hyötyä pimeissä paikoissa.")

    elif esine.nimi == "Kompassi":

        print("\nKompassi toimii normaalisti.")
        print("Sen avulla voi suunnistaa saarella.")

    elif esine.nimi == "Avain":

        print("\nVanha metallinen avain.")
        print("Et tiedä vielä, mihin se sopii.")

    elif esine.nimi == "Päiväkirja":

        print("\nTutkijan päiväkirja.")
        print("Viimeisessä merkinnässä lukee:")
        print('"Olen löytänyt jotain uskomatonta.')
        print('Minun täytyy tutkia asiaa majakalla."')

    elif esine.nimi == "Paristot":

        print("\nParistot näyttävät vielä käyttökelpoisilta.")

    elif esine.nimi == "Tutkimusraportti":

        print("\nTutkimusraportissa kerrotaan")
        print("oudosta energialähteestä saaren alla.")
        print("Tutkija uskoo, että se liittyy majakkaan.")

    elif esine.nimi == "Sulake":

        print("\nVanha sulake.")
        print("Se kuuluu laboratorion sähköjärjestelmään.")

    elif esine.nimi == "Laboratorion avain":

        print("\nAvain, jossa lukee:")
        print('"Laboratorio B".')

    elif esine.nimi == "Vanha radiolaite":

        print("\nVanha radiolaite.")
        print("Se näyttää olevan todella vanha.")

    elif esine.nimi == "Tutkijan muistiinpano":

        print("\nTutkijan muistiinpano:")
        print('"Jos löydät tämän,')
        print('olen todennäköisesti majakan kellarissa."')

    else:

        print("\nEt löydä esineestä mitään erityistä.")


def tutki_paikka(pelaaja):

    huone = pelaaja.sijainti

    if huone.nimi == "Lentokenttä":

        print("\n--- LENTOKENTTÄ ---")
        print("Mitä haluat tutkia?")
        print("1. Lentokone")
        print("2. Lähtöaula")
        print("3. Radiotorni")
        print("4. Peruuta")

        valinta = input("Valitse: ")

        if valinta == "1":

            print("\nLentokone on tyhjä.")
            print("Ohjaajan paikalla on paperilappu.")
            print('Lapussa lukee:')
            print('"Jos tutkijaa ei löydy, tarkista majakka."')

        elif valinta == "2":

            print("\nLähtöaulassa on vanha ilmoitustaulu.")
            print("Sen kartassa näkyy majakka.")

        elif valinta == "3":

            print("\nRadiotorni näyttää olevan pois käytöstä.")

        elif valinta == "4":

            print("Päätit olla tutkimatta tätä paikkaa.")

        else:

            print("Virheellinen valinta.")

    elif huone.nimi == "Tutkijan mökki":

        print("\n--- TUTKIJAN MÖKKI ---")
        print("Mitä haluat tutkia?")
        print("1. Työpöytä")
        print("2. Kirjahylly")
        print("3. Makuuhuone")
        print("4. Peruuta")

        valinta = input("Valitse: ")

        if valinta == "1":

            print("\nTyöpöytä on täynnä papereita.")
            print("Yhdessä paperissa lukee:")
            print('"Tutkimukseni ovat vieneet minut majakalle."')

        elif valinta == "2":

            print("\nKirjahyllyssä on kirjoja saaren historiasta.")
            print("Yksi kirja kertoo vanhasta majakasta.")

        elif valinta == "3":

            print("\nMakuuhuone on tyhjä.")
            print("Tutkija ei ole ollut täällä vähään aikaan.")

        elif valinta == "4":

            print("Päätit olla tutkimatta tätä paikkaa.")

        else:

            print("Virheellinen valinta.")

    elif huone.nimi == "Laboratorio":

        print("\n--- LABORATORIO ---")
        print("Mitä haluat tutkia?")
        print("1. Tietokone")
        print("2. Sähkökaappi")
        print("3. Tutkimuspöytä")
        print("4. Peruuta")

        valinta = input("Valitse: ")

        if valinta == "1":

            print("\nTietokoneella on tutkijan tutkimusraportti.")
            print("Raportissa kerrotaan uudesta")
            print("energialähteestä majakan alla.")
            print("Tutkija on kirjoittanut:")
            print('"Tämä voi olla elämäni tärkein löytö."')

        elif valinta == "2":

            print("\nSähkökaappi näyttää vanhalta.")
            print("Sen ympärillä on paljon johtoja.")

        elif valinta == "3":

            print("\nTutkimuspöydällä on erilaisia mittalaitteita.")
            print("Kaikki näyttää liittyvän majakan tutkimiseen.")

        elif valinta == "4":

            print("Päätit olla tutkimatta tätä paikkaa.")

        else:

            print("Virheellinen valinta.")

    elif huone.nimi == "Majakka":

        print("\n--- MAJAKKA ---")
        print("Mitä haluat tutkia?")
        print("1. Radiolaite")
        print("2. Majakan yläosa")
        print("3. Kellari")
        print("4. Peruuta")

        valinta = input("Valitse: ")

        if valinta == "1":

            print("\nVanha radiolaite on pölyinen.")
            print("Sen vieressä on pieni paperilappu.")
            print('Lapussa lukee:')
            print('"Olen lähellä löytöäni."')

        elif valinta == "2":

            print("\nMajakan valo pyörii hitaasti.")
            print("Ulos katsoessasi näet koko saaren.")

        elif valinta == "3":

            print("\nLaskeudut majakan kellariin.")
            print("Kellari on pimeä.")
            print("Perältä kuuluu ääni.")

            print("\nLöydät tutkijan!")
            print("Hän näyttää väsyneeltä, mutta on kunnossa.")

            print("\nTutkija kertoo:")
            print('"Löysin täältä jotain uskomatonta."')
            print('"Majakan alla on uusi luonnollinen')
            print('energialähde, jota ei ole koskaan ennen löydetty."')

            print("\nTutkija kertoo tutkineensa löytöä")
            print("jo useita päiviä.")

            print("Hän pyytää sinua auttamaan")
            print("hänet takaisin lentokentälle.")

            print("\n==============================")
            print("        PELI LÄPI!")
            print("==============================")

            print("\nLöysit tutkijan ja hänen uuden löytönsä.")
            print("Tehtäväsi on onnistuneesti suoritettu.")

            return True

        elif valinta == "4":

            print("Päätit olla tutkimatta tätä paikkaa.")

        else:

            print("Virheellinen valinta.")

    return False


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


def pelivalikko():

    print("\n--- PELIVALIKKO ---")
    print("1. Tutki paikkaa")
    print("2. Liiku")
    print("3. Näytä esineet")
    print("4. Tallenna peli")
    print("5. Palaa päävalikkoon")


def pelaa():

    lue_intro()
    lue_ohjeet()

    pelaaja, mokki, laboratorio, majakka = luo_peli()

    print("\n==============================")
    print("       PELI ALKAA!")
    print("==============================")

    print(f"\nTervetuloa, {pelaaja.nimi}!")

    print("Tehtäväsi on löytää kadonnut tutkija.")

    while True:

        pelivalikko()

        valinta = input("\nValitse toiminto: ")

        if valinta == "1":

            peli_loppui = tutki_paikka(pelaaja)

            if peli_loppui:
                break

            if len(pelaaja.sijainti.esineet) > 0:

                print("\nPaikassa on myös esineitä.")

                vastaus = input(
                    "Haluatko katsoa esineitä? (k/e): "
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

            if len(pelaaja.esineet) > 0:

                vastaus = input(
                    "Haluatko tutkia jotakin esinettä? (k/e): "
                )

                if vastaus.lower() == "k":

                    try:

                        numero = int(
                            input("Minkä esineen haluat tutkia? ")
                        )

                        if 1 <= numero <= len(pelaaja.esineet):

                            esine = pelaaja.esineet[numero - 1]

                            tutki_esine(esine)

                        else:

                            print("Virheellinen numero.")

                    except ValueError:

                        print("Anna numero.")

        elif valinta == "4":

            tallenna_peli(pelaaja)

        elif valinta == "5":

            print("\nPalaat päävalikkoon.")

            break

        else:

            print("Virheellinen valinta.")


def paavalikko():

    while True:

        print("\n")
        print("==============================")
        print("       KADONNUT TUTKIJA")
        print("==============================")

        print("1. Pelaa")
        print("2. Ohjeet")
        print("3. Lopeta")

        valinta = input("\nValitse: ")

        if valinta == "1":

            pelaa()

        elif valinta == "2":

            print("\n--- OHJEET ---")
            lue_ohjeet()

        elif valinta == "3":

            print("\nPeli lopetetaan.")
            print("Kiitos pelaamisesta!")

            break

        else:

            print("\nVirheellinen valinta.")


paavalikko()