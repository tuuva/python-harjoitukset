
def suurin(luvut):

    suurin_luku = luvut[0]

    for luku in luvut:
        if luku > suurin_luku:
            suurin_luku = luku

    return suurin_luku


luvut = [7, 3, 15, 2, 11, 9]

tulos = suurin(luvut)
print(f"suurin luku on: {tulos}")