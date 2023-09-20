def temperatura_promedio(ciudades):
    # Inicializar un diccionario para almacenar las temperaturas promedio de cada ciudad
    temperaturas_promedio = {}

    # Iterar a través de la lista de ciudades
    for ciudad, semanas in ciudades.items():
        # Inicializar una variable para almacenar la suma de temperaturas
        suma_temperaturas = 0

        # Contar el número de temperaturas en todas las semanas
        numero_temperaturas = 0

        # Iterar a través de las semanas de temperaturas
        for semana in semanas:
            # Sumar las temperaturas de la semana
            suma_temperaturas += sum(semana)
            # Contar el número de temperaturas en la semana
            numero_temperaturas += len(semana)

        # Calcular la temperatura promedio para la ciudad
        promedio_ciudad = suma_temperaturas / numero_temperaturas

        # Agregar el promedio al diccionario de temperaturas promedio
        temperaturas_promedio[ciudad] = promedio_ciudad

    return temperaturas_promedio

# Ejemplo de datos de temperaturas de 3 ciudades durante 4 semanas
datos_ciudades = {
    'Ciudad A': [ # 4 semanas y 7 días
        [20, 25, 22, 24, 23, 21, 23],
        [22, 26, 23, 25, 24, 22, 26],
        [21, 24, 22, 23, 23, 25, 23],
        [19, 23, 20, 22, 24, 21, 24]
    ],
    'Ciudad B': [ # 4 semanas y 7 días
        [18, 20, 19, 17, 19, 20, 21],
        [19, 22, 20, 18, 22, 19, 20],
        [17, 21, 19, 17, 23, 20, 22],
        [16, 19, 18, 15, 19, 21, 18]
    ],
    'Ciudad C': [ # 4 semanas y 7 días
        [25, 28, 27, 26, 22, 21, 24],
        [27, 30, 28, 29, 26, 23, 25],
        [26, 29, 27, 28, 25, 22, 23],
        [24, 28, 26, 25, 27, 21, 25]
    ]
}

# Calcular las temperaturas promedio de las ciudades
resultados = temperatura_promedio(datos_ciudades)

# Imprimir los resultados
for ciudad, promedio in resultados.items():
    print(f'Temperatura promedio en {ciudad}: {promedio:.2f} grados Celsius')