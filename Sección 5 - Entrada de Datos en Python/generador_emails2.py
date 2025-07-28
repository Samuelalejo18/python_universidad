print("*** Generador de emails ***")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_empresa = input("Ingrese nombre de la empresa: ")
dominio = input("Ingrese dominio de la empresa: ")

nombre_formateado = nombre.strip().lower().replace(" ", ".")
apellido_formateado = apellido.strip().lower().replace(" ", ".")

nombre_empresa = nombre_empresa.strip().lower().replace(" ", "")
dominio = dominio.strip().lower().replace(" ", "")

email = f"{nombre_formateado}.{apellido_formateado}@{nombre_empresa}{dominio}"
print(f'''
Tu nuevo email generado por el sistema es:
    {email}
    Felicidades!''')
