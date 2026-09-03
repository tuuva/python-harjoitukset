
oikea_käyttäjätunnus = "Python"
oikea_salasana = "Rules"

yritykset = 0

while yritykset < 5:
   käyttäjätunnus = str(input("Anna käyttäjätunnus: "))
   salasana = str(input("Anna salasana: "))
   
   yritykset = yritykset + 1
   
   if käyttäjätunnus == oikea_käyttäjätunnus and salasana == oikea_salasana:
         print("tervetuloa!")
         break
   
   else:
       print("Pääsy evätty")