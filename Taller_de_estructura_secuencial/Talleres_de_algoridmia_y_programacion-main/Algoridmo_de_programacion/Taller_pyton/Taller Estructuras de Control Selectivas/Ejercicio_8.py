def verificar_expresion(P, Q):
    # Calcular la expresión P^3 + Q^4 - 2*P^2
    resultado = P**3 + Q**4 - 2 * (P**2)
    
    # Verificar si la expresión es mayor que 680
    if resultado > 680:
        return "P y Q satisfacen la expresión: P = " + str(P) + " y Q = " + str(Q)
    else:
        return "P y Q no satisfacen la expresión: P = " + str(P) + " y Q = " + str(Q)

# Entrada de datos
P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))

# Llamada a la función para verificar la expresión
resultado = verificar_expresion(P, Q)

# Mostrar el resultado
print(resultado)
