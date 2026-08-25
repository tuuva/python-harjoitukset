##Yksi leiviskä on 20 naulaa.
##Yksi naula on 32 luotia.
##Yksi luoti on 13,3 grammaa.

leiviskät = float(input("Anna leiviskät"))
naulat = float(input("Anna naulat"))
luodit = float(input("Anna luodit"))

##leiviskät * 20 naulaa
##naulat * 32 luotia
##luodit * 13.3 grammaa

Naulat_lasku = (leiviskät * 20)
Luodit_lasku = ((naulat + Naulat_lasku) * 32)
Grammat_lasku = ((luodit + Luodit_lasku) * 13.3)

Kilogramma = (Grammat_lasku // 1000)
jakojäännös = (Grammat_lasku % 1000)

print(f"Grammat {Grammat_lasku}")
print(f"{Kilogramma}kilogrammaa {jakojäännös} grammaa")
