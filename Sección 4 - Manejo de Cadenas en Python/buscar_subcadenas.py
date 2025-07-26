cadena = "hola, mundo!"
posicion = cadena.find("mundo")
print(f"posicion: {posicion}")

# si se repite la palabra, solo devolver la posicion de la primera ocurrencia
cadena = "hola, mundo mundo mundo"
indice = cadena.find("mundo")
print(f"indice: {indice}")

# Obtener el indice de la subcadena de hola
indice_hola = cadena.find("hola")
print(f"el indice de la subcadena de hola: {indice_hola}")
