
def gallona_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

while True:

   gallonat = float(input("Anna gallonamäärä: "))

   if gallonat < 0:
     break
   
   litrat = gallona_litroiksi(gallonat)

   print(f"{litrat} litraa")
   

