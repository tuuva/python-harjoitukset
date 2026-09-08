import math

def yksikköhinta(hinta, halkaisija):
    halkaisija_m = halkaisija / 100
    säde = halkaisija_m / 2
    pinta_ala = math.pi * säde **2
    yksikköhinta = hinta / pinta_ala 

    return yksikköhinta

halkaisija_1 = float(input("Kerro ensimmäisen pizzan halkaisija senttimetreinä?: "))
hinta_1 = float(input("Kerro ensimmäisen pizzan hinta?"))

halkaisija_2 = float(input("Kerro toisen pizzan halkaisija senttimetreinä?: "))
hinta_2 = float(input("Kerro toisen pizzan hinta?"))

yksikköhinta_1 = yksikköhinta(hinta_1, halkaisija_1)
yksikköhinta_2 = yksikköhinta(hinta_2, halkaisija_2)

if yksikköhinta_1 < yksikköhinta_2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")

elif yksikköhinta_1 == yksikköhinta_2:
    print("Yksikköhinnat ovat samat")

else:
    print("Toinen pizza antaa paremman vastineen rahalle")

