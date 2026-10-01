##Peliprojekti
esineet = []


def pelaa():
    print()
    print("Peli alkaa!")
    print("Löysit kolme esinettä")
    print()
    print("1. lyhty")
    print("2. taikajuoma")
    print("3. avain")

    while True:
        valinta = input("Minkä otat mukaasi?: ")

        if valinta == "1" or valinta == "lyhty":
            esineet.append("lyhty")
            break

        elif valinta == "2" or valinta == "taikajuoma":
            esineet.append("taikajuoma")
            break

        elif valinta == "3" or valinta == "avain":
            esineet.append("avain")
            break

        else:
            print("Väärä valinta!")
            print("Valitse 1. lyhty, 2. taikajuoma tai 3. avain")

    print()
    nayta_esineet()

    if "avain" in esineet:
        print("Käytät avainta ja avaat oven!")
        print("Oven takana on pimeä huone.")
        print("Astut sisään, kun yhtäkkiä lattia alkaa sortua!")
        print("Sinun täytyy toimia nopeasti.")
        print("1. Juokse eteenpäin")
        print("2. Palaa takaisin")

    elif "taikajuoma" in esineet:
        print("Ovi on lukossa.")
        print("Jatkat matkaa, ja saavut metsään.")
        print("Edessäsi on kaksi polkua.")
        print("1. Vasen polku")
        print("2. Oikea polku")

        polku = input("Kumman valitset?: ")

        if polku == "1":
            print("Kuljet vasenta polkua pitkin.")
            print("Hetken päästä löydät salaisen luolan.")
            print("Luolan edessä seisoo vanha velho, joka pyytää apuasi.")
            print("1. Lupaan auttaa velhoa")
            print("2. Jatkan matkaa")

        elif polku == "2":
            print("Kuljet oikeaa polkua pitkin.")
            print("Tulet vanhalle sillalle.")
            print("Sillalla makaa haavoittunut henkilö.")
            print("Hän pyytää apuasi.")
            print("1. Autan häntä")
            print("2. Jatkan matkaa")

    elif "lyhty" in esineet:
        print("Ovi on lukossa.")
        print("Jatkat matkaa, ja saavut metsään.")
        print("Edessäsi on kaksi polkua.")
        print("1. Vasen polku")
        print("2. Oikea polku")

        polku = input("Kumman valitset?: ")

        if polku == "1":
            print("Kuljet vasenta polkua pitkin.")
            print("Hetken päästä tulet luolan suulle.")
            print("Luolan edessä seisoo vanha velho, joka pyytää sinua näyttämään tietä luolaan lyhdyn kanssa.")
            print("1. Lähden lyhtyni kanssa näyttämään tietä")
            print("2. Jatkan matkaa metsässä yksin")

        elif polku == "2":
            print("Kuljet oikeaa polkua pitkin.")
            print("Tulet vanhalle sillalle, jossa makaa haavoittunut henkilö.")
            print("Hän pyytää taikajuomaa vaivaansa, ja voisi vastineeksi näyttää sinulle turvallisen reitin metsän läpi ")
            print("1. Annan hänelle taikajuoman")
            print("2. Jatkan matkaa metsässä yksin")


def nayta_esineet():
    print("Mukanasi olevat esineet:")

    for esine in esineet:
        print("-", esine)


def ohjeet():
    print("Tässä pelissä sinun tehtäväsi on voittaa!")


def lopeta():
    print("Peli lopetetaan.")


ikä = int(input("Kuinka vanha olet?: "))

käyttäjänimi = input("Mikä on nimesi?: ")

print(f"Pelaajan nimi on {käyttäjänimi}, ja ikä {ikä}")


if ikä < 12:
    print("Olet alaikäinen, pääsy evätty")

else:
    print("Tervetuloa!")

    while True:
        print()
        print("1. pelaa")
        print("2. ohjeet")
        print("3. lopeta")

        komento = input("Anna komento: ")

        if komento == "lopeta":
            lopeta()
            break

        elif komento == "pelaa":
            pelaa()

        elif komento == "ohjeet":
            ohjeet()
            break

        else:
            print("Väärä komento!")
            print("Valitse pelaa, ohjeet tai lopeta.")