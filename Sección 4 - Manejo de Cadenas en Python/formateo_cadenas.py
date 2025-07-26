# Formato de cadenas

nombre = "samuel"
edad = 20

# f-string
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)

# string .format()


mensaje = "Hola  me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje)

mensaje = "Hola  me llamo {nombre} y tengo {edad} años.".format(nombre=nombre, edad=edad)
print(mensaje)

mensaje = "Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje.format(nombre=nombre, edad=edad))
