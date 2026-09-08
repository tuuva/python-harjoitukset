
def averages(luvut):
    avg = sum(luvut) / len(luvut)
    return avg

def average_grade(luvut):
    keskiarvot = []
    for alkio in luvut:
        keskiarvo = averages(alkio)
        keskiarvot.append(keskiarvo)

    return keskiarvot

lista = [1.0, 2.0, 2.0],[1.3,3.6,4.5]

keskiarvot = average_grade(lista)

for keskiarvo in keskiarvot:
    print(f"Keskiarvo: {keskiarvo: .2f}")



