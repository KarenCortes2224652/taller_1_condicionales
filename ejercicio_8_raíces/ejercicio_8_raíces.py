"""problema No.8: 
elaborar un programa que obtenga las raices de una ecuación de segundo grado """

print("-------------------------------------")
print("------LAS RAICES DE UNA ECUACIÓN ----")
print("-----------DE SEGUNDO GRADO----------")
import math

print("\n una ecuacion de segundo grado es de la forma ax^2+bx+c=0\n")
Q = input("ingrese el valor de a:")
Q = float(Q)
W = input("ingrese el valor de b:")
W = float(W)
E = input("ingrese el valor de c:")
E = float(E)
R = float((W*W)-(4*(Q)*(E)))

if R < 0:
    print("la ecuacion tiene solucion en los complejos")
elif R > 0:
    if Q != 0:
        if W != 0:
            x1 = (-(W) + math.sqrt((W*W)-(4*(Q)(E)))) / (2(Q))
            x1 = float(x1)
            x2 = (-(W) - math.sqrt((W*W)-(4*(Q)(E))))/(2(Q)) 
            x2 = float(x2)
            print("x1 = "+str(x1))
            print("x2 = "+str(x2))
        else:
             print("La ecuación tiene solo solución en los números complejos")
    else:
        print("La ecuación tiene solo solución en los números complejos")
else:
    print("La ecuación tiene solo solución en los números complejos")
