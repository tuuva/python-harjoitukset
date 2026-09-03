
luvut = []

luku = input("Anna luku: ")

while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku: ")

luvut.sort(reverse=True)

print("5 suurinta lukua suuruusjärjestyksessä: ")

for i in range(5):
    print(luvut[i])

