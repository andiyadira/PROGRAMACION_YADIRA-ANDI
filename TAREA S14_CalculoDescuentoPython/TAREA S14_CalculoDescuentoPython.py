# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    # Calcula el monto final después del descuento
    monto_final = monto_total - descuento
    # Devuelve el monto del descuento
    return descuento, monto_final

# Llamada a la función con solo el monto total de la compra
monto_compra1 = 1000
descuento1, monto_final1 = calcular_descuento(monto_compra1)
print(f'Monto de la compra: ${monto_compra1}')
print(f'Descuento aplicado: ${descuento1}')
print(f'Monto final a pagar: ${monto_final1}')

# Llamada a la función con el monto total de la compra y un porcentaje de descuento personalizado
monto_compra2 = 1500
porcentaje_descuento2 = 15
descuento2, monto_final2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
print(f'Monto de la compra: ${monto_compra2}')
print(f'Descuento aplicado: ${descuento2}')
print(f'Monto final a pagar: ${monto_final2}')