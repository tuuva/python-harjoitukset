luku = input("Anna luku: ")

suurin = float(luku)
pienin = float(luku)

luku = input("Anna luku: ")

while luku != "":
    luku = float(luku)
    
    if luku > suurin:
       suurin = luku
    
    if luku < pienin: 
       pienin = luku
    
    luku = input("Anna luku: ")

print(f"pienin: {pienin}")
print(f"Suurin: {suurin}")

