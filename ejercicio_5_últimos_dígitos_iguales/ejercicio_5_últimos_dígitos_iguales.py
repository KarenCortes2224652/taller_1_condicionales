#Ejercicio No.5: Determine si sus dos últimos dígitos son iguales.

print("------------------------------------------------------------")
print("------LOS-DOS-ULTIMOS-DIGITOS-DE-UN-NUMERO-SON-IGUALES------")
print("------------------------------------------------------------")

#input
número =int(input("Digite el valor de el número: "))

# processing
último_digito = int(str(número)[-1])
penúltimo_digito = int(str(número)[-2])

# output
if último_digito == penúltimo_digito:
    print("son iguales")
else:
    print("son dierentes")