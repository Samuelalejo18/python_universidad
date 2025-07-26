# Inmutabilidad en cadenas

cadena1 = "Hola mundo cadena1"
# adena1[5] = "h" # No podemos modificar los caracteres

#Pero si re asginar valor, pero se crea una nueva
cadena2 = cadena1
cadena1 = "Adios"
print(cadena2)
print(cadena1)

