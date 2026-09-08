import random

# Funktio joka palauttaa satunnaisen nopan silmäluvun väliltä 1..6

def nopanheitto():
    heitto = random.randint(1,6)
    return heitto

print(nopanheitto)

# Heittää noppaa kunnes tulos on kuusi

# Tulostaa joka heiton jälkeen silmäluvun

while True:
    tulos = nopanheitto()
    print(tulos)
    if tulos == 6:
        break


