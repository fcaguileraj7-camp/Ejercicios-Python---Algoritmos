
def construir_cadena(max):
    cad = ""
    for i in range(2, max+1):
        cad += f"{i},"
    return cad.rstrip(",")

def quitar_cadena(str, num):
    cad = ""
    for n in str.split(","):
        if n != num:
            if int(n) % int(num) != 0:
                cad += f"{n},"
        else:
            cad += f"{n},"

    return cad.rstrip(",")



MAX = int(input("Ingresa un numero de 1 a 100:"))
str = construir_cadena(MAX)
for snum in str.split(","):
    str= quitar_cadena(str, snum)

print(str)