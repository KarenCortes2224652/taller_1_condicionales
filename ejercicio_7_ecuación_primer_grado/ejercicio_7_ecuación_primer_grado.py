#Ejercicio No.7:Resolver una ecuación de primer grado.


print("-------------------------------------")
print("------ECUACIÓN-DE-PRIMER-GRADO-------")
print("-------------------------------------")

A = int(input("Ingresar el valor de A: "))
B = int(input("Ingresar el valor de B: "))



if(A != 0):
    H = (-1*B) / A;
    print("Solución de ecuaciones: "+ str(H))

else:
    print("Solución indeterminada");