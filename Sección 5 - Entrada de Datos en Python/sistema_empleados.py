print("***sistema de empleados")
nombre_empleado = input("Introduce tu nombre empleado: ")
edad_empleado = int(input("Introduce tu edad empleado: "))
salario_empleado = float(input("Introduce tu salario empleado: "))
es_jefe_departamento = input("Es jefe_departamento: (si/no) ")
# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower()

if es_jefe_departamento == "si":
    es_jefe_departamento = True
else:
    es_jefe_departamento = False
# es_jefe_departamento = es_jefe_departamento == "si"
# Imprimir los valores del Empleado
print("\n Datos del empleado")
print(f"Nombre del empleado: {nombre_empleado}")
print(f"Edaad del empleado: {edad_empleado}")
print(f"Salario del empleado: {salario_empleado: .2f}")
print(f"Es jefe dedepartamento: {es_jefe_departamento}")
