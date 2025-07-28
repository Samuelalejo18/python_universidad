from random import randint

print("*** Sistema Generador de ID Unico ***")
nombre = input("Ingresa su nombre: ")
apellido = input("Ingresa su apellido: ")
anno_naciimento = input("Ingresa su año de nacimiento (YYYY): ")

nombre = nombre.strip()
nombre_dos_digitos = nombre.upper()[0:2]

apellido = apellido.strip()
apellido_dos_digitos = apellido.upper()[0:2]
anno_naciimento = anno_naciimento.strip()[2:4]

numrandom = randint(0, 9999)
id_unico = f"{nombre_dos_digitos}{apellido_dos_digitos}{anno_naciimento}{numrandom}"

resultado_mensaje = f""" Hola,{nombre}
    Tu nuevo numero de identificacion (ID) generado por el sistema es:
    {id_unico}
    Felicidades!   
"""
print(resultado_mensaje)
