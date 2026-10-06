
def parilliset():

    luvut = []

    for i in range (5):
        luku = int(input("Anna luku: "))
        luvut.append(luku)

    for luku in luvut:
        if luku % 2 == 0:
            print(luku)

        
parilliset()

