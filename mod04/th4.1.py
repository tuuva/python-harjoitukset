# kysy kalastajalta kuhan pituus senttimetreinä
kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä."))
# arvio onko kuha alamittainen
if kuhan_pituus < 37:
    print("Laske kuha järveen.")
# lasketaan puuttuva pituus
mitat = (37 - kuhan_pituus)
if kuhan_pituus < 37:
    print(f"mitoista jaa uupumaan {mitat}")




