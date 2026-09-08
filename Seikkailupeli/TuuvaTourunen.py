##Peliprojekti
esineet = []

def pelaa():
    print("Peli alkaa!")
    print("Löysit kolme esinettä") 
    print("1. miekka")
    print("2. taikajuoma")
    print("3. avain")

    valinta = str(input("Minkä otat mukaasi?: "))

    if valinta == "1":
        esineet.append("miekka")

    elif valinta == "2":
            esineet.append("taikajuoma")

    elif valinta == "3":
            esineet.append("avain")

    nayta_esineet()

    if "avain" in esineet:
         print("Käytät avainta ja avaat oven!")
         print("Oven takana on pimeä huone.")
         print("Astut sisään, kun yhtäkkiä lattia alkaa sortua!")
         print("Sinun täytyy toimia nopeasti.")
         print("1. Juokse eteenpäin")
         print("2. Palaa takaisin")


    else:
         print("Ovi on lukossa.")
         print("Jatkat matkaa,ja saavut metsään.")
         print("Edessäsi on kaksi polkua.")
         print("1. Vasen polku")
         print("2. Oikea polku")

         polku = input("Kumman valitset?: ")

         if polku == "1":
              print("Kuljet vasenta polkua pitkin.")
              print("Hetken päästä löydät salaisen luolan")
              print("Luolan edessä seisoo vanha velho, hän näyttää väsyneeltä ja pyytää apuasi.")
              print("'Tarvitsen apuasi. Olen menettänyt taikasauvani luolaan.'")
              print("1. Lupaan auttaa velhoa")
              print("2. Jatkan matkaa")

         elif polku == "2":
              print("Kuljet oikeaa polkua pitkin.")
              print("Tulet vanhalle sillalle.") 
              print("Sillalla makaa haavoittunut mies.")
              print("Hän nostaa katseensa ja sanoo:")
              print("'Auta minut pois täältä, niin annan sinulle jotain arvokasta.'")
              print("1. Autan häntä")
              print("2. Jatkan matkaa")

def nayta_esineet():
    print("Mukanasi olevat esineet:")
    
    for esine in esineet:
         print("-", esine)
    
def ohjeet():
    print("Tässä pelissä sinun tehtäväsi on voittaa!")

def lopeta():
    print("Peli lopetetaan.")


ikä = int(input("Kuinka vanha olet?: "))

käyttäjänimi = str(input("Mikä on nimesi?: "))

print(f"pelaajan nimi on {käyttäjänimi}, ja ikä {ikä}")

if ikä < 12:
    print("Olet alaikäinen, pääsy evätty")

else:
    print("Tervetuloa!")
    print("1. pelaa")
    print("2. ohjeet")
    print("3. lopeta")

while True:
    
    komento = input("Anna komento: ")

    print("1. pelaa")
    print("2. ohjeet")
    print("3. lopeta")
    
    if komento == "lopeta":
        lopeta()
        break
    elif komento == "pelaa":
        pelaa()
    elif komento == "ohjeet":
        ohjeet()
