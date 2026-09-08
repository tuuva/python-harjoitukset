
def vain_parilliset(luvut):
    parilliset = []

    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset

luvut = [1, 5, 6, 8, 11, 17, 20, 31, 7]

parilliset = vain_parilliset(luvut)


print(f"lista {luvut}")
print(f"karsittu lista {parilliset}")



    