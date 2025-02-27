def calcular_nuevo_sueldo(sueldo):
    # Determinar el aumento según el sueldo
    if sueldo < 900000:
        aumento = 0.15  # 15% de aumento
    else:
        aumento = 0.12  # 12% de aumento
    
    # Calcular el nuevo sueldo
    nuevo_sueldo = sueldo * (1 + aumento)
    
    return nuevo_sueldo

# Entrada de datos
sueldo = float(input("Ingrese el sueldo del trabajador en COP: "))

# Llamada a la función para calcular el nuevo sueldo
nuevo_sueldo = calcular_nuevo_sueldo(sueldo)

# Imprimir el nuevo sueldo
print(f"El nuevo sueldo del trabajador es: {nuevo_sueldo:.2f} COP")
