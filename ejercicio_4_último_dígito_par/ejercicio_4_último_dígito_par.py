#EJERCICIO No 4: Determine si si último dígito es un número par

print("--------------------------------------")
print("------ÚLTIMO_DIGITO_PAR---------------")
print("--------------------------------------")

# input

X = int(input("DIGITE EL VALOR DE NUMERO ENTERO: "))

# proccesing

Último_dígito = X % 10 
S = Último_dígito % 2

if S == 0:
    print("El último dígito de: " + str(X) + "NÚMERO PAR" )

if S!= 0:
    print("El último dígito de: " + str(X) + "NÚMERO IMPAR")