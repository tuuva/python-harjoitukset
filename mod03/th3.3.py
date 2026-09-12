import math
##suorakulmion kanta ja korkeus
kanta = float(input("Mikä on suorakulmion kanta?"))
korkeus = float(input("Mikä on suorakulmion korkeus?"))

##tulostaa piirin ja pinta-alan
piiri = (kanta + korkeus + kanta + korkeus)

pinta_ala = (kanta * korkeus)

print(f"suorakulmion piiri on {piiri}, ja sen pinta-ala on {pinta_ala}")

