sukupuoli = str(input("mikä on sinun sukupuoli?"))
hemoglobiini = float(input("mikä on sinun hemoglobiiniarvo?"))
if hemoglobiini > 117 and hemoglobiini <= 175 and sukupuoli == "nainen":
    print("arvosi ovat normaalit.")
elif hemoglobiini < 117 and sukupuoli == "nainen":
    print("arvosi ovat matalat.")
elif hemoglobiini > 175 and sukupuoli == "nainen":
    print("arvosi ovat korkeat")

if hemoglobiini > 134 and hemoglobiini <= 195 and sukupuoli == "mies":
    print("arvosi ovat normaalit.")
elif hemoglobiini < 134 and sukupuoli == "mies":
    print("arvosi ovat matalat")
elif hemoglobiini > 195 and sukupuoli == "mies":
    print("arvosi ovat korkeat.")


