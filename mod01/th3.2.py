import math 

##Pyydä käyttäjältä ympyrän säde ja tallenna muuttujaan
circle_radius_input = float(input("Anna säteen pituus senttimetreinä "))
radius_float = float(circle_radius_input)

## Laske ymoyrän pinta-ala
## pi * säde potenssiin kaksi
area = (math.pi * radius_float**2)

## Tulosta ympyrän pinta-ala
print(f"Pinta-ala on: {area}")
