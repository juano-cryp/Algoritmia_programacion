def calcular_pago(lectura_anterior, lectura_actual):
    # Validar que la lectura actual sea mayor que la anterior
    if lectura_actual < lectura_anterior:
        return "Error: La lectura actual debe ser mayor o igual a la anterior."

    # Calcular el consumo de energía
    consumo = lectura_actual - lectura_anterior
    monto_total = 0

    # Aplicar tarifas por rango
    if consumo <= 100:
        monto_total = consumo * 4600
    elif consumo <= 300:
        monto_total = (100 * 4600) + ((consumo - 100) * 80000)
    elif consumo <= 500:
        monto_total = (100 * 4600) + (200 * 80000) + ((consumo - 300) * 100000)
    else:
        monto_total = (100 * 4600) + (200 * 80000) + (200 * 100000) + ((consumo - 500) * 120000)

    return f"Consumo: {consumo} Kwh\nMonto a pagar: {monto_total:,} COP"  # Formato con separadores de miles

# Entrada del usuario
lectura_anterior = int(input("Ingrese la lectura anterior (Kwh): "))
lectura_actual = int(input("Ingrese la lectura actual (Kwh): "))

# Cálculo y resultado
resultado = calcular_pago(lectura_anterior, lectura_actual)
print(resultado)
