contador = 0

for i in range(50):
    c =input(f"Ingrese la palabra: {i+1}:")
    
    if c == 'a':
        contador += 1
        
print ("Cantidad de veces que aparece 'a':", contador)