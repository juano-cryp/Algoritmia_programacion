# Inicializar listas y variables para almacenar los datos
nombres = []
puntajes = []
total_estudiantes = 0
suma_puntajes = 0

# Bucle para ingresar los datos de los estudiantes
while True:
    # Paso 1: Solicitar nombre y puntaje
    nombre = input("Introduce el nombre del estudiante: ")
    puntaje = float(input(f"Introduce el puntaje de {nombre}: "))
    
    # Almacenar los datos
    nombres.insert(nombre)
    puntajes.insert(puntaje)
    
    # Actualizar el total de estudiantes y la suma de puntajes
    total_estudiantes += 1
    suma_puntajes += puntaje
    
    # Preguntar si desea continuar
    continuar = input("¿Desea ingresar otro estudiante? (Sí/No): ").strip().lower()
    if continuar != 'sí':
        break
# Puntaje máximo y mínimo
puntaje_maximo = max(puntajes)
puntaje_minimo = min(puntajes)

# Estudiantes con puntaje máximo y mínimo
nombre_max = nombres[puntajes.index(puntaje_maximo)]
nombre_min = nombres[puntajes.index(puntaje_minimo)]

# Promedio de puntajes
promedio_puntajes = suma_puntajes / total_estudiantes

# Porcentaje de estudiantes con puntajes inferiores y superiores al promedio
estudiantes_inferiores = sum(1 for p in puntajes if p < promedio_puntajes)
estudiantes_superiores = sum(1 for p in puntajes if p > promedio_puntajes)

porcentaje_inferiores = (estudiantes_inferiores / total_estudiantes) * 100
porcentaje_superiores = (estudiantes_superiores / total_estudiantes) * 100

print("\nEstadísticas de la prueba de admisión:")
print(f"Nombre del estudiante con el puntaje más alto: {nombre_max} (Puntaje: {puntaje_maximo})")
print(f"Nombre del estudiante con el puntaje más bajo: {nombre_min} (Puntaje: {puntaje_minimo})")
print(f"Puntaje máximo obtenido: {puntaje_maximo}")
print(f"Puntaje mínimo obtenido: {puntaje_minimo}")
print(f"Promedio de todos los puntajes: {promedio_puntajes:.2f}")
print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {porcentaje_inferiores:.2f}%")
print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {porcentaje_superiores:.2f}%")
