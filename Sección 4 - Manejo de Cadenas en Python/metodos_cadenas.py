cadena = "hola, Mundo!"
otra_cadena = "python123"
solo_letras = "Python"
solo_numeros = "123456"
espacios = "   "
mayusculas = "PYTHON"
minusculas = "python"
titulo = "Hola Mundo"
vacía = ""
lineas = "Línea1\nLínea2\nLínea3"
separado_por_guiones = "uno-dos-tres"

print(f"Cadena original: '{cadena}'\n")
print(f"capitalize(): '{cadena.capitalize()}'")  # Primera letra mayúscula
print(f"casefold(): '{cadena.casefold()}'")      # Como lower pero más agresivo
print(f"center(30, '*'): '{cadena.center(30, '*')}'")  # Centra el texto con relleno
print(f"count('o'): {cadena.count('o')}")         # Cuenta ocurrencias
print(f"endswith('!'): {cadena.endswith('!')}")  # ¿Termina con...?
print(f"expandtabs(4): '{'Hola\tMundo'.expandtabs(4)}'")  # Expande tabulaciones
print(f"find('Mundo'): {cadena.find('Mundo')}")   # Posición o -1 si no está
print(f"index('Mundo'): {cadena.index('Mundo')}") # Igual a find, pero lanza error si no está
print(f"isalnum() - '{otra_cadena}': {otra_cadena.isalnum()}")  # Alfanumérico
print(f"isalpha() - '{solo_letras}': {solo_letras.isalpha()}")  # Solo letras
print(f"isdecimal() - '{solo_numeros}': {solo_numeros.isdecimal()}")  # Solo decimales
print(f"isdigit() - '{solo_numeros}': {solo_numeros.isdigit()}")      # Solo dígitos
print(f"isidentifier() - 'variable1': {'variable1'.isidentifier()}")  # ¿Nombre válido?
print(f"islower() - '{minusculas}': {minusculas.islower()}")   # Solo minúsculas
print(f"isupper() - '{mayusculas}': {mayusculas.isupper()}")   # Solo mayúsculas
print(f"isspace() - '{espacios}': {espacios.isspace()}")       # Solo espacios
print(f"istitle() - '{titulo}': {titulo.istitle()}")           # ¿Formato título?
print(f"join(['Hola', 'Mundo']): {'-'.join(['Hola', 'Mundo'])}")  # Une lista
print(f"ljust(20, '-'): '{cadena.ljust(20, '-')}'")            # Alinea a izquierda
print(f"rjust(20, '-'): '{cadena.rjust(20, '-')}'")            # Alinea a derecha
print(f"lower(): '{cadena.lower()}'")                         # Todo a minúsculas
print(f"upper(): '{cadena.upper()}'")                         # Todo a mayúsculas
print(f"lstrip(): '{cadena.lstrip()}'")                       # Quita espacios izquierda
print(f"rstrip(): '{cadena.rstrip()}'")                       # Quita espacios derecha
print(f"strip(): '{cadena.strip()}'")                         # Quita espacios ambos lados
print(f"partition(','): {cadena.partition(',')}")             # Divide en 3 partes (antes, separador, después)
print(f"rpartition(','): {cadena.rpartition(',')}")           # Igual pero desde el final
print(f"replace('Mundo', 'Samuel'): '{cadena.replace('Mundo', 'Samuel')}'")  # Reemplaza
print(f"split(): {cadena.split()}")                           # Divide por espacios
print(f"split(','): {cadena.split(',')}")                     # Divide por coma
print(f"rsplit(','): {cadena.rsplit(',')}")                   # Divide desde la derecha
print(f"splitlines(): {lineas.splitlines()}")                 # Divide por líneas
print(f"startswith('  Hola'): {cadena.startswith('  Hola')}") # ¿Empieza con...?
print(f"swapcase(): '{cadena.swapcase()}'")                   # Invierte mayúsculas y minúsculas
print(f"title(): '{cadena.title()}'")                         # Formato título
print(f"translate(str.maketrans('o', '0')): '{cadena.translate(str.maketrans('o', '0'))}'")  # Traducción de caracteres
print(f"zfill(20): '{solo_numeros.zfill(20)}'")               # Rellena con ceros a la izquierda
