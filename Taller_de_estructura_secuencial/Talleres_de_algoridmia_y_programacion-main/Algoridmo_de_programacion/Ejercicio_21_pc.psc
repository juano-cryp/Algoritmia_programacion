Proceso CalcularPorcentajeRecargo
    // Declaración de variables
    Definir P, T, totalCuotas, recargo, porcentajeRecargo Como Real
	
    // Entrada de datos
    Escribir "Ingrese el precio de compra al contado (P): "
    Leer P
    Escribir "Ingrese el valor de cada cuota mensual (T): "
    Leer T
	
    // Cálculo del total a pagar por cuotas
    totalCuotas <- T * 12
	
    // Cálculo del recargo total
    recargo <- totalCuotas - P
	
    // Cálculo del porcentaje de recargo
    porcentajeRecargo <- (recargo / P) * 100
	
    // Mostrar resultados
    Escribir "--------------------------------------------------"
    Escribir "Precio de contado: ", P, " COP"
    Escribir "Total a pagar por cuotas: ", totalCuotas, " COP"
    Escribir "Recargo total: ", recargo, " COP"
    Escribir "Porcentaje de recargo: ", porcentajeRecargo, " %"
    Escribir "--------------------------------------------------"
FinProceso

