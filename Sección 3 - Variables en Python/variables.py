# Variables en Python

# Declaracion e inicializacion de variables

edad = 20
altura = 1.75
pais = "Colombia"

# Acceder a las variables
print("Valores iniciales")
print("edad:", edad)
print("altura:", altura)
print("pais:", pais)

#Modificar el valor de una variable

edad=25
altura = 1.80
pais = "Venezuela"
print(" ")
print("Valores modificados:")
print("edad:", edad)
print("altura:", altura)
print("pais:", pais)

#En python el tipo es dinamico
print(" ")
edad= "Treinta"
print("edad:", edad)

# Si queremos accedes al valor de una variables no declarada mandara error
telefono= "3333434"
print("telefono:", telefono)
print(" ")




# objeto
persona = {
    "edad": edad,
    "altura": altura,
    "pais": pais
}
edad = 21
persona["edad"] = 40
print("objeto persona:")
print("edad:", persona["edad"])
print("altura:", persona["altura"])
print("pais:", persona["pais"])
