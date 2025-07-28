# Reto cocina
print(f"*** Receta de cocina ***")
nombre_receta = input("Ingresa el nombre: ")
ingredientes_receta = input("Ingresa el ingrediente: ")
minutos_preparacion_receta = int(input("Ingresa el tiempo de preparacion (min): "))
dificultades = ["Facil", "Media", "Alta"]
dificultad_receta = input("Ingresa el dificultad: ")

# Convertimos la lista original a minúsculas para comparar
dificultades_lower = [d.lower() for d in dificultades]

if dificultad_receta not in dificultades_lower:
    dificultad_receta = "Dificultad no encontrada"
else:
    # Para mostrarlo con la primera letra en mayúscula
    dificultad_receta = dificultad_receta.capitalize()

print(f"-------------------------------------")
print(f"Nombre receta: {nombre_receta}")
print(f"Ingredientes receta: {ingredientes_receta}")
print(f"Tiempo de preparacion: {minutos_preparacion_receta}")
print(f"Dificultad: {dificultad_receta}")
