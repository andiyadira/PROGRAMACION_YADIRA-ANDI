# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "Nombre": "José Calero",
    "Edad": 30,
    "Ciudad": "Lago Agrio"
}

# Acceder al valor de "ciudad" y modificarlo
informacion_personal["Ciudad"] = "Nueva Loja"

# Agregar una nueva clave-valor para "profesion"
informacion_personal["Profesión"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "062-830-910"

# Eliminar la clave "edad"
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

# Imprimir el diccionario final
print("Diccionario Final:")
print(informacion_personal)
