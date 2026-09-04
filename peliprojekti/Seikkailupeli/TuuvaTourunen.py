##Peliprojekti

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
        break
    elif komento == "pelaa":
        print("Peli alkaa!")
    elif komento == "ohjeet":
        print("Tässä pelissä sinun tehtäväsi on voittaa!")
