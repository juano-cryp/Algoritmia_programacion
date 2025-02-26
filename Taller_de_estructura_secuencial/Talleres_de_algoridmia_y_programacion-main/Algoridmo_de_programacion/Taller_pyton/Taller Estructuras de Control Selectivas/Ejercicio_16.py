import math

def resolver_ecuacion_segundo_grado(a, b, c):
    if a == 0:
        return "Error: El coeficiente A no puede ser 0 en una ecuación de segundo grado."

    # Calcular la discriminante
    d = (b ** 2) - (4 * a * c)

    # Evaluar la discriminante
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Dos soluciones reales: X1 = {x1}, X2 = {x2}"
    elif d == 0:
        x = -b / (2 * a)
        return f"Única solución real: X = {x}"
    else:
        return "No tiene solución en los números reales (raíces complejas)."

# Entrada del usuario
a = float(input("Ingrese el coeficiente A: "))
b = float(input("Ingrese el coeficiente B: "))
c = float(input("Ingrese el coeficiente C: "))

# Resolución y resultado
resultado = resolver_ecuacion_segundo_grado(a, b, c)
print(resultado)
