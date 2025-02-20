Proceso CalcularPorcentajeGanancia
    // Declaración de variables
    Definir X, u, K Como Real
    Definir costoTotal, ganancia, porcentajeGanancia Como Real
	
    // Entrada de datos
    Escribir "Ingrese la cantidad de naranjas compradas (X): "
    Leer X
    Escribir "Ingrese el costo por docena de naranjas (Bs): "
    Leer u
    Escribir "Ingrese el total obtenido por la venta de las naranjas (Bs): "
    Leer K
	
    // Cálculo del costo total de la compra
    costoTotal <- (X / 12) * u
	
    // Cálculo de la ganancia obtenida
    ganancia <- K - costoTotal
	
    // Cálculo del porcentaje de ganancia
    porcentajeGanancia <- (ganancia / costoTotal) * 100
	
    // Mostrar resultados
    Escribir "--------------------------------------------------"
    Escribir "Costo total de la compra: ", costoTotal, " Bs"
    Escribir "Ganancia obtenida: ", ganancia, " Bs"
    Escribir "Porcentaje de ganancia: ", porcentajeGanancia, " %"
    Escribir "--------------------------------------------------"
FinProceso

