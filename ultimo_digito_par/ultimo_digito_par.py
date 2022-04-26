"""Problema No.3: 
Verificar si el ultimo digito de un numero es PAR"""

#input 
x = int(input (" Digite el valor de x: "))

#Proseccing 
ultimo_digito = x % 10 
r = ultimo_digito % 2 

if r == 0:
    print("El ultimo digito de " + str(x) + "es PAR")

print("eso era...")


