
luku = int(input("Anna kokonaisluku: "))

alkuluku = True

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        alkuluku = False


if alkuluku:
    print("On alkuluku.")

else:
    print("Ei ole alkuluku.")

    



