def yli_rajan(luvut, raja):

    yli = []

    for luku in luvut:
        if luku > raja:
            yli.append(luku)

    return yli


raja = 10
luvut = [4, 12, 7, 19, 3, 25, 8]

yli = yli_rajan(luvut, raja)

print(f"alkuperäinen lista: {luvut}")
print(f"yli rajan: {yli}")