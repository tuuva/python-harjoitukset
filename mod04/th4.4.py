vuosiluku = float(input("Anna vuosiluku?"))
if vuosiluku <100 and vuosiluku % 4 == 0 or vuosiluku >100 and vuosiluku % 400 == 0:
    print("On karkausvuosi.")
else:
    print("Ei ole karkausvuosi")

