def lasku():
    yli = []

    for luku in luvut:
        if luku > 8:
            yli.append(luku)

    return yli


luvut = [4, 7, 12, 3, 9, 20]

tulos = lasku()

print(f"Yli 8 olevat luvut: {tulos}")