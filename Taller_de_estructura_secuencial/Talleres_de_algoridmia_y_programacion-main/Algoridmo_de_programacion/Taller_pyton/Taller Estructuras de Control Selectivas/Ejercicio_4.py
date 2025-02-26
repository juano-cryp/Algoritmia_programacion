def calcular_pago_compra(monto_total):
    # Inicialización de variables
    if monto_total > 5000000:
        # La compra excede los $5.000.000 COP
        inversion_empresa = monto_total * 0.05
        prestamo_banco = monto_total * 0.30
        pago_credito = monto_total - inversion_empresa - prestamo_banco
    else:
        # La compra no excede los $5.000.000 COP
        inversion_empresa = monto_total * 0.70
        pago_credito = monto_total * 0.30
        prestamo_banco = 0  # No hay préstamo del banco
    
    # Intereses sobre el pago al crédito
    intereses_credito = pago_credito * 0.20
    
    # Mostrar los resultados
    return {
        "Inversion_empresa": inversion_empresa,
        "Pago_credito": pago_credito,
        "Intereses_credito": intereses_credito,
        "Prestamo_banco": prestamo_banco
    }

# Entrada de datos
monto_total = float(input("Ingrese el monto total de la compra en COP: "))

# Llamada a la función para calcular los pagos
resultado = calcular_pago_compra(monto_total)

# Mostrar los resultados
print(f"Cantidad a invertir de los fondos de la empresa: {resultado['Inversion_empresa']:.2f} COP")
print(f"Cantidad a pagar a crédito al fabricante: {resultado['Pago_credito']:.2f} COP")
print(f"Monto a pagar por intereses: {resultado['Intereses_credito']:.2f} COP")
if resultado["Prestamo_banco"] > 0:
    print(f"Cantidad prestada al banco: {resultado['Prestamo_banco']:.2f} COP")
else:
    print("No se requiere préstamo del banco.")
