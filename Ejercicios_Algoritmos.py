#Capital e interes

c = float(input("Ingrese monto de capital:"))
i = float(input("Ingrese monto de interes:"))
m = int (input("Ingrese los años:"))

capital = c

for _ in range(m):
    capital = capital + capital *(i/100)

print("El capital final es:", capital)