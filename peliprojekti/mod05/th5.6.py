import random

pisteet = int(input("Kuinka monta pistettä arvotaan?"))

i = 0
ympyrässä = 0

while i < pisteet:
    y = random.randint(-1000,1000)/1000
    x = random.randint(-1000,1000)/1000
    
    print(x,y)

    if x * x + y * y < 1:
        ympyrässä = ympyrässä + 1

    i = i + 1

pii = 4 * ympyrässä / pisteet
print(f"Piin likiarvo on: {pii}")



