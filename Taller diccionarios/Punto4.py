def gestionar_notas():
    estudiantes = {}
    num_estudiantes = 0

    print("Ingrese las notas de los estudiantes (máximo 10).")

    while num_estudiantes < 10:
        num_estudiantes += 1
        nombre = input(f"Ingrese el nombre del estudiante {num_estudiantes}: ")
        while True:
            try:
                nota_str = input(f"Ingrese la nota de {nombre}: ")
                try:
                    nota = float(nota_str)
                except ValueError:
                    nota = float(nota_str.replace(',', '.')) # Usamos replace solo si la conversión inicial falla

                if 0 <= nota <= 10:
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido para la nota.")

        estudiantes[str(num_estudiantes)] = {"nombre": nombre, "nota": nota}

        continuar = input("¿Desea ingresar otro estudiante? (s/n): ").lower()
        if continuar != 's':
            break

    aprobados = []
    suspensos = []
    suma_notas = 0

    for info_estudiante in estudiantes.values():
        nombre = info_estudiante["nombre"]
        nota = info_estudiante["nota"]
        suma_notas += nota
        if nota >= 5:
            aprobados.append(nombre)
        else:
            suspensos.append(nombre)

    if estudiantes:
        nota_media = suma_notas / len(estudiantes)
        print("\n Resultados")
        print("Estudiantes aprobados:", ", ".join(aprobados))
        print("Estudiantes suspensos:", ", ".join(suspensos))
        print(f"Nota media de la clase: {nota_media:.2f}")
    else:
        print("\nNo se ingresaron notas de estudiantes.")

if __name__ == "__main__":
    gestionar_notas()