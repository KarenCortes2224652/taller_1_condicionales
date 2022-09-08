#Ejercicio No 3: Positivo de 4 dígitos.

print("----------------------------")
print("---DETERMINE-SI-ES-UN-NÚMERO-POSITIVO-DE-4-DÍGITOS---")
print("----------------------------")

# input

F = int(input("Digite el valor del número entero: "))

#   Processing 
if 999 < F < 10000:
    G = (" El número digitado tiene cuatro dígitos")
else:
    G = (" El número digitado no tiene 4 dígitos ")

# output

print("El numero es " + str(F) + G)