
lentoasemat = {
    "EFHK": "Helsinki-Vantaa",
    "EFRO": "Rovaniemi",
    "EFTP": "Tampere-Pirkkala",
    "EFIV": "Ivalo",
    "EFKU": "Kuopio",
    "EFJO": "Joensuu",
    "EFJY": "Jyväskylä",
    "EFOU": "Oulu",
    "EFTU": "Turku",
    "EFVA": "Vaasa",
    "EGLL": "London Heathrow",
    "EGKK": "London Gatwick",
    "LFPG": "Paris Charles de Gaulle",
    "EDDF": "Frankfurt",
    "EHAM": "Amsterdam Schiphol",
    "ESSA": "Stockholm Arlanda",
    "ENGM": "Oslo Gardermoen",
    "KJFK": "New York JFK",
    "KLAX": "Los Angeles International",
    "KORD": "Chicago O'Hare",
    "RJTT": "Tokyo Haneda",
    "YSSY": "Sydney"
}

while True:
    toiminto = input("Valitse toiminto (1 = uusi lentoasema, 2 = hae lentoasema, 3 = lopeta): ")

    if toiminto == "1":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "2":
        icao = input("Anna ICAO-koodi: ")

        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löydy.")

    elif toiminto == "3":
        break

