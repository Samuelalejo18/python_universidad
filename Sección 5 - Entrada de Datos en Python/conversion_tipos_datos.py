# Conversion de tipos de datos

# Convertir de candena a numero

numero_cadena = "10"
numero_entero = int(numero_cadena)
print(f"Valor numerico en cadena :{numero_cadena}  y tipo:{type(numero_cadena)} ")
print(f"Valor numerico a entero :{numero_entero} y tipo:{type(numero_entero)}\n ")

# Convertir de cadena a flotante
flotante_cadena = "3.14"
flotante_entero = float(flotante_cadena)
print(f"Valor flotante en cadena :{flotante_cadena} y tipo:{type(flotante_cadena)} ")
print(f"Valor numerico a flotante :{flotante_entero} y tipo:{type(flotante_entero)}\n ")

# Convertir numero  a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f"valor entero {numero_entero} y tipo:{type(numero_entero)} ")
print(f"valor numero a cadena {numero_cadena} y tipo:{type(numero_cadena)}\n ")

# Convertir a booleano
# Tipo bool es falso en los siguientes casos:
# Si el valor es 0,cadena vacia, o None, entonces regresa False
numero_entero = 0
booleano = bool(numero_entero)
print(f"valor numero_entero {numero_entero} y tipo:{type(numero_entero)} ")
print(f"valor booleano  {booleano} y tipo:{type(booleano)}\n ")

cadena = ""  # El largo de la cadena es 0
booleano_cadena = bool(cadena)  # Si el largo de la cadena es 0 regresa False
print(f"valor vadena '{cadena}' y tipo:{type(cadena)} ")
print(f"valor booleano cadena {booleano_cadena} y tipo:{type(booleano_cadena)}\n ")

none = None
booleano_none = bool(none)
print(f"valor de none  '{none}' y tipo:{type(none)} ")
print(f"valor booleano none {booleano_none} y tipo:{type(booleano_none)}\n ")

# Tipo bool es verdadero en los siguientes casos:
# Regresa True, si el valor es distinto de 0, distinto de cadena vacia
# Tambien y si es distinto de None

numero_entero = 1
booleano = bool(numero_entero)
print(f"valor numero entero {numero_entero} y tipo:{type(numero_entero)} ")
print(f"valor booleano numero '{booleano}' y tipo:{type(booleano)}\n ")

cadena = "cadena para booleano con valor"  # El largo de la cadena es mayor a 0
booleano_cadena = bool(cadena)  # Si el largo de la cadena es  mayor a 0 regresa True
print(f"valor vadena '{cadena}' y tipo:{type(cadena)} ")
print(f"valor booleano de  cadena no vacia {booleano_cadena} y tipo:{type(booleano_cadena)}\n ")

# Convertir de flotante a entero
# Se trunca la parte decimal
flotante = 9.99
entero = int(flotante)
print(f"valor flotante: {flotante} y tipo: {type(flotante)}")
print(f"valor flotante a entero: {entero} y tipo: {type(entero)}\n")

# Convertir de entero a flotante
entero = 7
flotante = float(entero)
print(f"valor entero: {entero} y tipo: {type(entero)}")
print(f"valor entero a flotante: {flotante} y tipo: {type(flotante)}\n")

# Convertir lista a cadena
# (Usando .join() si es de strings)
lista = ["Hola", "mundo"]
cadena = " ".join(lista)
print(f"valor lista: {lista} y tipo: {type(lista)}")
print(f"valor lista a cadena: '{cadena}' y tipo: {type(cadena)}\n")

# Convertir cadena a lista
# (Separando por caracteres o usando .split() para separar por espacios u otro delimitador)
cadena = "Hola mundo"
lista = list(cadena)
print(f"valor cadena: '{cadena}' y tipo: {type(cadena)}")
print(f"valor cadena a lista: {lista} y tipo: {type(lista)}\n")

# O usando split():
cadena = "Hola mundo desde Python"
lista_palabras = cadena.split()
print(f"valor cadena: '{cadena}' y tipo: {type(cadena)}")
# Convertir tupla a lista y lista a tupla
tupla = (1, 2, 3)
print(f"valor cadena a lista por palabras: {lista_palabras} y tipo: {type(lista_palabras)}\n")

lista = list(tupla)
print(f"valor tupla: {tupla} y tipo: {type(tupla)}")
print(f"valor tupla a lista: {lista} y tipo: {type(lista)}\n")

nueva_tupla = tuple(lista)
print(f"valor lista: {lista} y tipo: {type(lista)}")
print(f"valor lista a tupla: {nueva_tupla} y tipo: {type(nueva_tupla)}\n")

# Convertir set (conjunto) a lista o tupla
conjunto = {1, 2, 3}
lista_desde_set = list(conjunto)
tupla_desde_set = tuple(conjunto)
print(f"valor set: {conjunto} y tipo: {type(conjunto)}")
print(f"set a lista: {lista_desde_set} y tipo: {type(lista_desde_set)}")
print(f"set a tupla: {tupla_desde_set} y tipo: {type(tupla_desde_set)}\n")

# Convertir diccionario a lista de claves o valores
diccionario = {"a": 1, "b": 2}
claves = list(diccionario.keys())
valores = list(diccionario.values())
print(f"valor diccionario: {diccionario} y tipo: {type(diccionario)}")
print(f"diccionario a lista de claves: {claves}")
print(f"diccionario a lista de valores: {valores}\n")
