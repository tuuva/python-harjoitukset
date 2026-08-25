ika = int(input("Anna ika"))
laji = str(input("Anna laji"))
if ika >=18 and laji == "ihminen":
    print("Voit tilata viiniä")
elif ika >=100 and laji == "tonttu":
    print("Voit tilata olutta")
elif laji == "robotti":
    print("Voit tilata öljyä")
elif ika >0 and laji == "robotti" or laji == "ihminen" or laji == "tonttu":
    print("Voit tilata kahvia")
        