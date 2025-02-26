def calcular_incentivos(ventas_departamento1, ventas_departamento2, ventas_departamento3, salario_bruto):
    # Calcular las ventas totales
    ventas_totales = ventas_departamento1 + ventas_departamento2 + ventas_departamento3
    
    # Calcular el 33% de las ventas totales
    limite_ventas = ventas_totales * 0.33
    
    # Determinar el incentivo por departamento
    incentivo1 = 0
    incentivo2 = 0
    incentivo3 = 0
    
    if ventas_departamento1 > limite_ventas:
        incentivo1 = salario_bruto * 0.20
    
    if ventas_departamento2 > limite_ventas:
        incentivo2 = salario_bruto * 0.20
    
    if ventas_departamento3 > limite_ventas:
        incentivo3 = salario_bruto * 0.20
    
    # Calcular los salarios finales con incentivos
    salario_final1 = salario_bruto + incentivo1
    salario_final2 = salario_bruto + incentivo2
    salario_final3 = salario_bruto + incentivo3
    
    # Mostrar resultados
    return {
        "Salario_final_departamento1": salario_final1,
        "Salario_final_departamento2": salario_final2,
        "Salario_final_departamento3": salario_final3
    }

# Entrada de datos
ventas_departamento1 = float(input("Ingrese el total de ventas del departamento 1: "))
ventas_departamento2 = float(input("Ingrese el total de ventas del departamento 2: "))
ventas_departamento3 = float(input("Ingrese el total de ventas del departamento 3: "))
salario_bruto = float(input("Ingrese el salario bruto mensual de los vendedores: "))

# Llamada a la función para calcular los salarios finales con incentivos
resultado = calcular_incentivos(ventas_departamento1, ventas_departamento2, ventas_departamento3, salario_bruto)

# Mostrar los resultados
print(f"Salario final del departamento 1: {resultado['Salario_final_departamento1']:.2f} COP")
print(f"Salario final del departamento 2: {resultado['Salario_final_departamento2']:.2f} COP")
print(f"Salario final del departamento 3: {resultado['Salario_final_departamento3']:.2f} COP")
