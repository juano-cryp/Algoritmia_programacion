def redondear_a_centena(A, B, C, D):
    # Formar el número N a partir de A, B, C y D
    N = 1000 * A + 100 * B + 10 * C + D
    
    # Obtener la parte de las centenas, decenas y unidades
    centenas = (N // 100) * 100
    decenas = (N % 100) // 10
    
    # Redondear dependiendo del valor de las decenas
    if decenas >= 5:
        resultado = centenas + 100  # Redondeamos hacia arriba
    else:
        resultado = centenas  # Redondeamos hacia abajo
    
    return resultado

# Entrada de datos
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
D = int(input("Ingrese el valor de D: "))

# Llamada a la función para redondear el número
resultado = redondear_a_centena(A, B, C, D)

# Mostrar el resultado
print(f"El número redondeado a la centena más cercana es: {resultado}")
