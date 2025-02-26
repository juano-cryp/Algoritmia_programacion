def calcular_expresion(A, B, C, D):
    # Verificamos si D es igual a 0
    if D == 0:
        resultado = (A - C) ** 2
    # Si D es mayor que 0
    elif D > 0:
        resultado = (A - B ** 3) / D
    else:
        resultado = "Valor de D no válido"  # En caso de que D sea negativo
    
    return resultado

# Entrada de datos
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
D = int(input("Ingrese el valor de D: "))

# Llamada a la función para calcular la expresión
resultado = calcular_expresion(A, B, C, D)

# Mostrar el resultado
print(f"El resultado de la expresión es: {resultado}")
