# Generador de emails
print("*** Generador de Email ***")

# Nombre completo del usuario
nombre = " Samuel Alejandro Monsalve "
print(f"Nombre usuario: {nombre}")
empresa = " Global Mentoring "
dominio = ".com.mx"

nombre_usuario_normalizado = nombre.strip().lower().replace(" ", ".")

empresa_normalizado = empresa.replace(" ", "").lower()

dominio_normalizado = f"@{empresa_normalizado}{dominio}"

email = nombre_usuario_normalizado + dominio_normalizado

print(f"Nombre usuario normalizado: {nombre_usuario_normalizado}\n")

print(f"Nombre empresa: {empresa}")
print(f"Extension del dominio: {dominio}")
print(f"Dominion del email normalizado: {dominio_normalizado}")
print(f"Email final generado: {email}")
