# Punto No. 1: Llamada telefónica.
import math

print("-------------")
print("--- LLAMADA - TELEFÓNICA ---")
print("-------------")

#input
M=int(input("Digite el tiemppo de duración de su llamada:"))

#proseccing
if M>3:
    M= 300+(M-3)*50
else:
    M=300

#output
print("---------RESULTADOS---------")
print("Valor a pagar: "+str(M))