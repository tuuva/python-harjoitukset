cm = float(input("Anna senttimetrit: "))
tuuma = 0
   
while tuuma >= 0:
    tuuma = (cm * 2.54)
    if tuuma < 0:
        break
    print(f"{tuuma}")
    cm = float(input("Anna senttimetrit: "))
    
    print("Luku on negatiivinen")
    print("Toiminnot lopetettu")



