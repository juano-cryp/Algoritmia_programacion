# Inicializar variables para almacenar los datos
total_licor = 0
total_mujeres_menores_edad = 0
total_hombres_20_25_no_aguardiente = 0
total_edad_consumen_cerveza = 0
total_personas_consumen_cerveza = 0
total_personas_consumen_whisky = 0
total_encuestados = 0

# Bucle para realizar la encuesta
while True:
    # Paso 1: Solicitar datos al encuestado
    consume_licor = input("¿Consume licor? (Sí/No): ").strip().lower()
    if consume_licor != 'sí' and consume_licor != 'no':
        print("Por favor, ingrese 'Sí' o 'No'.")
        continue

    licor_preferido = int(input("¿Cuál es su licor preferido?\n1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro: "))
    edad = int(input("¿Cuál es su edad?: "))
    sexo = input("¿Cuál es su sexo? (Mujer/Hombre): ").strip().lower()

    # Asegurarnos de que los datos sean válidos
    if licor_preferido not in [1, 2, 3, 4, 5, 6]:
        print("Opción de licor no válida.")
        continue

    if sexo not in ['mujer', 'hombre']:
        print("Sexo no válido.")
        continue
    total_encuestados += 1

    # Total de personas que consumen licor
    if consume_licor == 'sí':
        total_licor += 1

    # Total de mujeres menores de edad
    if sexo == 'mujer' and edad < 18:
        total_mujeres_menores_edad += 1

    # Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años
    if sexo == 'hombre' and 20 <= edad <= 25 and licor_preferido != 1:
        total_hombres_20_25_no_aguardiente += 1

    # Promedio de edad de quienes consumen cerveza
    if licor_preferido == 3:  # Cerveza
        total_edad_consumen_cerveza += edad
        total_personas_consumen_cerveza += 1

    # Personas que consumen whisky
    if licor_preferido == 5:  # Whisky
        total_personas_consumen_whisky += 1

    
    continuar = input("¿Desea continuar con la encuesta? (Sí/No): ").strip().lower()
    if continuar != 'sí':
        break

# Calcular el promedio de edad de los que consumen cerveza
promedio_edad_cerveza = 0
if total_personas_consumen_cerveza > 0:
    promedio_edad_cerveza = total_edad_consumen_cerveza / total_personas_consumen_cerveza

# Calcular el porcentaje de personas que consumen whisky
porcentaje_whisky = 0
if total_encuestados > 0:
    porcentaje_whisky = (total_personas_consumen_whisky / total_encuestados) * 100

print("\nResultados de la encuesta:")
print(f"Total de personas que consumen licor: {total_licor}")
print(f"Total de mujeres menores de edad: {total_mujeres_menores_edad}")
print(f"Total de hombres entre 20 y 25 años que no consumen aguardiente: {total_hombres_20_25_no_aguardiente}")
print(f"Promedio de edad de quienes consumen cerveza: {promedio_edad_cerveza:.2f}")
print(f"Porcentaje de personas que consumen whisky: {porcentaje_whisky:.2f}%")
