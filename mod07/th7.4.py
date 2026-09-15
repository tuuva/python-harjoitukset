
def summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

lista = []

luku = input("Anna luku (tyhjä lopettaa): ")

while luku != "":
    lista.append(int(luku))
    luku = input("Anna luku: ")

tulos = summa(lista)
print(f"Summa on: {tulos}")


