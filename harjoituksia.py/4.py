def laske_parilliset(luvut):

    summa = 0

    for luku in luvut:
        if luku % 2 == 0:
            summa = summa + 1

    return summa

luvut = [3, 8, 12, 5, 7, 10, 4]

tulos = laske_parilliset(luvut)

print(f"parillisten lukujen määrä on: {tulos}")