# Ejercicio 6: Determinar si la suma de sus ultimas 2 cifras es es un número de 1 dígito.

print("---------------------------------")
print("---SUMA-ÚLTIMAS-2-CIFRAS---")
print("---------------------------------")

# input
K=int(input("Ingrese un valor:"))
#procesing
K2= K % 10
K1= (K % 100) // 10

suma = K1+K2

if suma>=1 and suma<=9:
    print("La suma de" ,K1, "y" ,K2,  " da: " + str(suma)+ " es un número de 1 dígito")
else:
    print("La suma de" ,K1,"y", K2," da: " +str(suma)+ " que no es un número de 1 dígito")

#finish