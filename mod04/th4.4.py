vuosiluku = float(input("Anna vuosiluku?"))
if vuosiluku % 4 == 0 or vuosiluku % 400 == 0:
    print("On karkausvuosi.")
else:
    print("Ei ole karkausvuosi")
