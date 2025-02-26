def calcular_descuento(nombre_cliente, monto_compra):
    # Inicializar el porcentaje de descuento y el monto a pagar
    descuento = 0
    
    # Determinar el descuento según el monto de la compra
    if monto_compra < 50000:
        descuento = 0
    elif 50000 <= monto_compra <= 100000:
        descuento = 0.05
    elif 100000 < monto_compra <= 700000:
        descuento = 0.11
    elif 700000 < monto_compra <= 1500000:
        descuento = 0.18
    else:  # Si el monto es mayor a 1.500.000
        descuento = 0.25
    
    # Calcular el descuento recibido
    monto_descuento = monto_compra * descuento
    # Calcular el monto a pagar después del descuento
    monto_a_pagar = monto_compra - monto_descuento
    
    # Mostrar los resultados
    return (f"Nombre del cliente: {nombre_cliente}\n"
            f"Monto de la compra: {monto_compra:.2f} COP\n"
            f"Descuento recibido: {monto_descuento:.2f} COP\n"
            f"Monto a pagar: {monto_a_pagar:.2f} COP")


# Entrada de datos
nombre_cliente = input("Ingrese el nombre del cliente: ")
monto_compra = float(input("Ingrese el monto de la compra en COP: "))

# Llamada a la función para calcular el descuento y mostrar los resultados
resultado = calcular_descuento(nombre_cliente, monto_compra)

# Mostrar el resultado
print(resultado)
