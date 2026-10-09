
# Tuodaan muiden moduulien luokat ja JSON-kirjasto käyttöön.
from pelaaja import Pelaaja
from huone import Huone
from esine import Esine
import json


# Luetaan pelin aloitustarina tekstitiedostosta.
def lue_intro():
    try:
        with open("peliprojekti/Seikkailupeli/peli/intro.txt", "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())

    # Käsitellään mahdolliset tiedostovirheet.
    except FileNotFoundError:
        print("Intro-tiedostoa ei löydy.")

    except IOError:
        print("Tiedoston lukemisessa tapahtui virhe.")


# Luetaan pelin ohjeet tekstitiedostosta.
def lue_ohjeet():
    try:
        with open("peliprojekti/Seikkailupeli/peli/ohjeet.txt", "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())

    except FileNotFoundError:
        print("Ohjeet-tiedostoa ei löydy.")

    except IOError:
        print("Tiedoston lukemisessa tapahtui virhe.")


# Kysytään nimeä niin kauan, että se on hyväksyttävä.
def kysy_nimi():
    while True:
        # strip() poistaa ylimääräiset välilyönnit alusta ja lopusta.
        nimi = input("Mikä on nimesi? ").strip()

        # Tarkistetaan, ettei nimi ole tyhjä, liian pitkä tai sisällä numeroita.
        if nimi and len(nimi) <= 50 and nimi.replace(" ", "").replace("-", "").isalpha():
            return nimi

        print("Anna nimi kirjaimilla (esim. Anna-Maija), ei numeroilla.")


# Tarkistetaan ikä. Ikärajan ulkopuolella pelaaminen lopetetaan.
def kysy_ika():
    while True:
        try:
            # int() muuttaa käyttäjän syötteen kokonaisluvuksi.
            ika = int(input("Kuinka vanha olet? "))

            if ika < 6:
                print("Alaikäinen.")
                return None

            elif ika > 100:
                print("Virheellinen ikä.")
                return None

            else:
                # Hyväksytty ikä palautetaan pääohjelmalle.
                return ika

        # Jos ikään syötetään esimerkiksi kirjaimia, kysytään uudelleen.
        except ValueError:
            print("Anna ikä numeroina, esimerkiksi 20.")


# Tallennetaan pelaajan tiedot JSON-tiedostoon.
def tallenna_peli(pelaaja, reitti):

    # Kootaan tallennettavat tiedot sanakirjaan.
    tallennus = {
        "nimi": pelaaja.nimi,
        "ika": pelaaja.ika,
        "sijainti": pelaaja.sijainti.nimi,
        "esineet": [],
        "reitti": reitti
    }

    # Käydään esinelista läpi ja tallennetaan esineiden nimet.
    for esine in pelaaja.esineet:
        tallennus["esineet"].append(esine.nimi)

    try:
        # w tarkoittaa kirjoitustilaa ja korvaa aiemman tallennuksen.
        with open("save.json", "w", encoding="utf-8") as tiedosto:
            json.dump(tallennus, tiedosto, ensure_ascii=False, indent=4)

        print("\nPelaajan tiedot tallennettu.")

    except IOError:
        print("Tietojen tallentaminen epäonnistui.")


# Tarkistetaan, löytyykö samalla nimellä aikaisempi tallennus.
def lataa_peli(nimi, lentokentta):
    try:
        # json.load() lukee tallennustiedoston Pythonin käyttöön.
        with open("save.json", "r", encoding="utf-8") as tiedosto:
            tallennus = json.load(tiedosto)

    # Jos tiedosto puuttuu tai on virheellinen, palautetaan None.
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return None

    # isinstance() tarkistaa, että tallennus on sanakirja.
    if not isinstance(tallennus, dict):
        return None

    # Varmistetaan, että tallennettu nimi vastaa annettua nimeä.
    if tallennus.get("nimi") != nimi:
        return None

    print("\nAiemmat pelaajatiedot löytyivät!")
    print(f"Edellinen reitti: {tallennus.get('reitti', 'Ei tiedossa')}")

    # Kysytään, haluaako pelaaja käyttää vanhoja tietoja.
    while True:
        vastaus = input("Haluatko käyttää aiempia tietojasi? (k/e): ").strip().lower()

        if vastaus == "k" or vastaus == "e":
            break

        print("Vastaa k tai e.")

    if vastaus == "e":
        return None

    # Tarkistetaan myös tallennetun iän kelvollisuus.
    try:
        ika = int(tallennus.get("ika", ""))

        if not 6 <= ika <= 100:
            raise ValueError

    except (ValueError, TypeError):
        print("Tallennetusta iästä puuttuu kelvollinen arvo.")
        return None

    # Luodaan Pelaaja-olio vanhoilla tiedoilla.
    pelaaja = Pelaaja(nimi=nimi, sijainti=lentokentta, ika=ika)

    # Haetaan tallennettu esinelista, oletuksena tyhjä lista.
    esineet = tallennus.get("esineet", [])

    # Palautetaan esineet nimien perusteella takaisin Esine-olioiksi.
    if isinstance(esineet, list):
        for esineen_nimi in esineet:
            if isinstance(esineen_nimi, str):
                pelaaja.kerää_esine(Esine(esineen_nimi))

    # Palautetaan valmis Pelaaja-olio pääohjelmalle.
    return pelaaja


# Kysytään yksinkertainen valinta reitin aikana.
def kysy_kaksi():
    while True:
        valinta = input("Valitse 1 tai 2: ").strip()

        if valinta == "1" or valinta == "2":
            return valinta

        print("Virheellinen valinta.")


# Kysytään, minkä kolmesta reitistä pelaaja valitsee.
def valitse_reitti():
    while True:
        print("\nMihin lähdet lentokentältä?")
        print("1. Tutkijan mökki")
        print("2. Laboratorio")
        print("3. Majakka")

        valinta = input("Valitse 1, 2 tai 3: ").strip()

        # Palautetaan hyväksytty valinta pääohjelmalle.
        if valinta == "1" or valinta == "2" or valinta == "3":
            return valinta

        print("Virheellinen valinta.")


# Ensimmäinen reitti: tutkijan mökki.
def mokin_reitti(pelaaja, mokki):

    # Kutsutaan Pelaaja-luokan metodia sijainnin muuttamiseen.
    pelaaja.liiku(mokki)

    print("\nMökissä näet pöydän ja kirjahyllyn.")
    print("1. Tutki pöytää")
    print("2. Tutki kirjahyllyä")

    valinta = kysy_kaksi()

    if valinta == "1":
        print("\nPöydällä on tutkijan päiväkirja.")
    else:
        print("\nKirjahyllystä löytyy tutkijan päiväkirja.")

    # Tarkistetaan, ettei pelaajalla ole samaa esinettä ennestään.
    if not pelaaja.onko_esine("Päiväkirja"):
        mokki.lisää_esine(Esine("Päiväkirja"))

        # Poimitaan esine huoneesta ja lisätään pelaajan listaan.
        pelaaja.kerää_esine(mokki.poimi_esine(1))

    print("Päiväkirjassa kerrotaan, että tutkija lähti majakalle.")
    print("Päätät seurata vihjettä.")

    # Palautetaan suoritetun reitin nimi.
    return "Tutkijan mökin kautta"


# Toinen reitti: laboratorio.
def laboratorion_reitti(pelaaja, laboratorio):

    pelaaja.liiku(laboratorio)

    print("\nLaboratoriossa näet tietokoneen ja tutkimuspöydän.")
    print("1. Tutki tietokonetta")
    print("2. Tutki tutkimuspöytää")

    valinta = kysy_kaksi()

    if valinta == "1":
        print("\nTietokoneelta löytyy tutkimusraportti.")
    else:
        print("\nTutkimuspöydältä löytyy tutkimusraportti.")

    # Lisätään tutkimusraportti vain, jos sitä ei vielä ole.
    if not pelaaja.onko_esine("Tutkimusraportti"):
        laboratorio.lisää_esine(Esine("Tutkimusraportti"))
        pelaaja.kerää_esine(laboratorio.poimi_esine(1))

    print("Raportissa kerrotaan saaren maaperän lämpöenergiasta.")
    print("Viimeinen merkintä johdattaa majakalle.")

    return "Laboratorion kautta"


# Kolmas reitti: suoraan majakalle.
def majakan_reitti(pelaaja, majakka):

    pelaaja.liiku(majakka)

    print("\nMajakan eteisessä on vanha radiolaite ja ilmoitustaulu.")
    print("1. Tutki radiolaitetta")
    print("2. Tutki ilmoitustaulua")

    valinta = kysy_kaksi()

    if valinta == "1":
        print("\nRadiolaitteesta kuuluu tutkijan heikko ääni.")
    else:
        print("\nIlmoitustaulussa on tutkijan jättämä viesti.")

    if not pelaaja.onko_esine("Tutkijan muistiinpano"):
        majakka.lisää_esine(Esine("Tutkijan muistiinpano"))
        pelaaja.kerää_esine(majakka.poimi_esine(1))

    print("Vihjeen perusteella tutkija saattaa olla majakan kellarissa.")

    return "Majakan kautta"


# Toinen vaihe: kaikki reitit johtavat majakalle.
def tutki_majakkaa(pelaaja, majakka):

    # Siirretään pelaaja majakalle, ellei hän ole jo siellä.
    if pelaaja.sijainti.nimi != "Majakka":
        pelaaja.liiku(majakka)

    print("\n--- MAJAKAN TUTKIMINEN ---")
    print("Majakka on hiljainen, mutta jostain kuuluu kolinaa.")
    print("1. Tutki eteistä")
    print("2. Tutki portaikkoa")

    valinta = kysy_kaksi()

    if valinta == "1":
        print("\nEteisestä löytyy taskulamppu.")
    else:
        print("\nPortaiden juurelta löytyy taskulamppu.")

    if not pelaaja.onko_esine("Taskulamppu"):
        majakka.lisää_esine(Esine("Taskulamppu"))
        pelaaja.kerää_esine(majakka.poimi_esine(1))

    print("Taskulampun valossa näet kellariin johtavan oven.")


# Kolmas vaihe: etsitään tutkija majakan kellarista.
def tutki_kellaria():

    print("\n--- MAJAKAN KELLARI ---")
    print("Avaat kellarin oven ja laskeudut portaita alas.")
    print("1. Tutki työpöytää")
    print("2. Seuraa kellarista kuuluvaa ääntä")

    valinta = kysy_kaksi()

    # Valinta muuttaa tarinaa, mutta molemmat johtavat tutkijan löytämiseen.
    if valinta == "1":
        print("\nTyöpöydällä on papereita energiantutkimuksesta.")
        print("Pöydän takaa kuuluu tutkijan ääni.")
    else:
        print("\nSeuraat ääntä kellarin takaosaan.")

    print("\nLöydät kadonneen tutkijan! Hän on kunnossa.")


# Loppuratkaisu etenee kolmessa lyhyessä osassa.
def pelin_loppu(pelaaja, reitti, lentokentta):

    print("\n--- TUTKIJAN LÖYTÖ ---")
    print("Tutkija kertoo löytäneensä saarelta lämpöenergiaa,")
    print("jota voitaisiin käyttää uusiutuvana energiana.")

    print("\nMitä haluat kysyä tutkijalta?")
    print("1. Mihin energiaa voisi käyttää?")
    print("2. Voiko sen käyttäminen vahingoittaa luontoa?")

    valinta = kysy_kaksi()

    if valinta == "1":
        print("\nTutkija: Sillä voitaisiin tuottaa lämpöä ja sähköä.")
    else:
        print("\nTutkija: Mahdolliset ympäristövaikutukset täytyy tutkia.")

    print("\n--- KESTÄVÄ KEHITYS ---")
    print("Tutkija aikoo selvittää, miten energiaa voisi hyödyntää")
    print("ilman että saaren luonto ja eläimet kärsivät.")

    print("\n--- PALUU LENTOKENTÄLLE ---")
    print("Autat tutkijan turvallisesti takaisin lentokentälle.")

    # Pelaajan sijainti muutetaan takaisin lentokentäksi.
    pelaaja.liiku(lentokentta)

    print("\n==========================")
    print("         PELI LÄPI!")
    print("==========================")
    print(f"Ratkaisit pelin: {reitti}.")

    # Tallennetaan pelaajan tiedot automaattisesti pelin päätyttyä.
    tallenna_peli(pelaaja, reitti)


# Aloitetaan peli ja ohjataan sen etenemistä.
def pelaa():

    lue_intro()
    lue_ohjeet()

    # Luodaan neljä Huone-luokan oliota.
    lentokentta = Huone("Lentokenttä")
    mokki = Huone("Tutkijan mökki")
    laboratorio = Huone("Laboratorio")
    majakka = Huone("Majakka")

    nimi = kysy_nimi()

    # Yritetään ladata aiemmin tallennettu Pelaaja-olio.
    pelaaja = lataa_peli(nimi, lentokentta)

    # Jos tallennusta ei löytynyt, luodaan uusi pelaaja.
    if pelaaja is None:
        ika = kysy_ika()

        # Jos ikä ei kelpaa, palautetaan False päävalikolle.
        if ika is None:
            print("Kirjattu ulos pelistä.")
            return False

        pelaaja = Pelaaja(nimi=nimi, sijainti=lentokentta, ika=ika)

    valinta = valitse_reitti()

    # Valinnan perusteella kutsutaan oikeaa reittifunktiota.
    if valinta == "1":
        reitti = mokin_reitti(pelaaja, mokki)

    elif valinta == "2":
        reitti = laboratorion_reitti(pelaaja, laboratorio)

    else:
        reitti = majakan_reitti(pelaaja, majakka)

    # Kaikki kolme reittiä jatkavat samoihin loppuvaiheisiin.
    tutki_majakkaa(pelaaja, majakka)
    tutki_kellaria()
    pelin_loppu(pelaaja, reitti, lentokentta)


# Päävalikossa voi pelata, lukea ohjeet tai lopettaa.
def paavalikko():

    while True:
        print("\n--- KADONNUT TUTKIJA ---")
        print("1. Pelaa")
        print("2. Ohjeet")
        print("3. Lopeta peli")

        valinta = input("Valitse: ").strip()

        if valinta == "1":
            # Jos pelaa() palauttaa False, lopetetaan päävalikon silmukka.
            if pelaa() is False:
                break

        elif valinta == "2":
            print("\n--- OHJEET ---")
            lue_ohjeet()

        elif valinta == "3":
            print("Kiitos pelaamisesta!")
            break

        else:
            print("Virheellinen valinta.")


# Käynnistetään ohjelma kutsumalla päävalikkoa.
paavalikko()
