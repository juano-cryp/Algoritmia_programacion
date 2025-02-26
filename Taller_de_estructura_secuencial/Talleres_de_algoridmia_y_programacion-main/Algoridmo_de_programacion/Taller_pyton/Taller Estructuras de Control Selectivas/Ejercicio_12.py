def desglosar_cop(cantidad):
    # Lista de billetes y monedas en orden descendente
    denominaciones = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
    
    resultado = {}  # Diccionario para almacenar la cantidad de cada billete/moneda usado

    # Redondear la cantidad para eliminar valores menores a 50 COP
    cantidad = cantidad - (cantidad % 50)

    for valor in denominaciones:
        if cantidad >= valor:
            cantidad_usada = cantidad // valor  # Número de billetes o monedas
            cantidad -= cantidad_usada * valor  # Restar del total
            resultado[valor] = cantidad_usada  # Guardar el resultado

    return resultado

# Ejemplo de uso
entrada = int(input("Ingrese la cantidad en COP: "))  # Pedir la cantidad al usuario
desglose = desglosar_cop(entrada)

# Mostrar los resultados
print("Desglose de billetes y monedas:")
for valor, cantidad in desglose.items():
    print(f"{cantidad} x {valor} COP")

