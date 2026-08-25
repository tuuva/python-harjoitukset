import math
##suorakulmion kanta ja korkeus
kanta = float(input("Mikä on suorakulmion kanta?"))
korkeus = float(input("Mikä on suorakulmion korkeus?"))

##tulostaa piirin ja pinta-alan
piiri = (kanta + korkeus + kanta + korkeus)

pintaala = (kanta * korkeus)

print(f"suorakulmion piiri on {piiri}, ja sen pintaala on {pintaala}")

