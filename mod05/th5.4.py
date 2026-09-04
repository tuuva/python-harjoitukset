import random
#Arvotaan pelin oikea vastaus

oikea_luku = random.randint(1,10)

luku = float(input("Arvaa luku 1- 10 väliltä: "))

oikea_luku = float(oikea_luku)

while luku != oikea_luku:

    if luku > oikea_luku:
        print("Luku on liian suuri")
    if luku < oikea_luku:
        print("Luku on liian pieni")

    luku = float(input("Arvaa luku 1-10 väliltä: "))

    if luku == oikea_luku:
        print("Oikein.")
    
    