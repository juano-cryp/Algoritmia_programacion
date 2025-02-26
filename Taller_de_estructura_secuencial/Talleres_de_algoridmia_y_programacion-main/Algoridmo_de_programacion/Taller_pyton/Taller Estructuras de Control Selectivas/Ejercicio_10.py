def calcular_aumento(categoria, sueldo_bruto):
    # Definir los aumentos según la categoría
    if categoria == 1 and sueldo_bruto == 5000000:
        aumento = 0.10  # 10% de aumento
    elif categoria == 2 and sueldo_bruto == 4300000:
        aumento = 0.15  # 15% de aumento
    elif categoria == 3 and sueldo_bruto == 3600000:
        aumento = 0.20  # 20% de aumento
    elif categoria == 4 and sueldo_bruto == 2000000:
        aumento = 0.40  # 40% de aumento
    elif categoria == 5 and sueldo_bruto == 900000:
        aumento = 0.60  # 60% de aumento
    else:
        return "Categoría o salario bruto no válido"
    
    # Calcular el aumento y el nuevo sueldo
    monto_aumento = sueldo_bruto * aumento
    nuevo_sueldo = sueldo_bruto + monto_aumento
    
    # Retornar los resultados
    return (f"Categoría: {categoria}\n"
            f"Sueldo Bruto: {sueldo_bruto:.2f} COP\n"
            f"Aumento: {monto_aumento:.2f} COP\n"
            f"Nuevo Sueldo: {nuevo_sueldo:.2f} COP")

# Entrada de datos
categoria = int(input("Ingrese la categoría del trabajador (1, 2, 3, 4, 5): "))
sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador en COP: "))

# Llamada a la función para calcular el aumento y mostrar los resultados
resultado = calcular_aumento(categoria, sueldo_bruto)

# Mostrar el resultado
print(resultado)
