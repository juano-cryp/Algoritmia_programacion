def verificar_anemia(edad, sexo, hemoglobina):
    if edad <= 1/12:  # 0 a 1 mes (convertimos 1 mes a fracción de año)
        rango_min, rango_max = 13, 26
    elif edad <= 6/12:  # Mayor de 1 mes y hasta 6 meses
        rango_min, rango_max = 10, 18
    elif edad <= 1:  # Mayor de 6 meses y hasta 12 meses
        rango_min, rango_max = 11, 15
    elif edad <= 5:  # Mayor de 1 año y hasta 5 años
        rango_min, rango_max = 11.5, 15
    elif edad <= 10:  # Mayor de 5 años y hasta 10 años
        rango_min, rango_max = 12.6, 15.5
    elif edad <= 15:  # Mayor de 10 años y hasta 15 años
        rango_min, rango_max = 13, 15.5
    elif sexo.lower() == "mujer":  # Mujeres mayores de 15 años
        rango_min, rango_max = 12, 16
    elif sexo.lower() == "hombre":  # Hombres mayores de 15 años
        rango_min, rango_max = 14, 18
    else:
        return "Error: Sexo no válido."

    # Evaluar si el nivel de hemoglobina está por debajo del rango
    if hemoglobina < rango_min:
        return f"Positivo para Anemia. Nivel bajo de hemoglobina ({hemoglobina} g%)."
    else:
        return f"Negativo para Anemia. Nivel normal de hemoglobina ({hemoglobina} g%)."

# Entrada del usuario
edad = float(input("Ingrese la edad en años (ejemplo: 0.5 para 6 meses, 2 para 2 años): "))
sexo = input("Ingrese el sexo (hombre/mujer): ")
hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

# Evaluación y resultado
resultado = verificar_anemia(edad, sexo, hemoglobina)
print(resultado)
