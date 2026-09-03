import random 

määrä = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0

for i in range(määrä):

    silmäluku = random.randint(1,6)

    summa = summa + silmäluku

    print(silmäluku)

print(f"Silmälukujen summa on: {summa}")
