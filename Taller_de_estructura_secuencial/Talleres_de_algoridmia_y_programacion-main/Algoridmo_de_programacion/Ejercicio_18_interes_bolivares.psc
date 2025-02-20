Proceso CalcularTasaInteres
    Definir capital, interesPagado, tiempo, tasaInteres Como Real
	
    // Entrada de datos
    Escribir "Ingrese el capital prestado (Bolívares): "
    Leer capital
    Escribir "Ingrese el total de intereses pagados (Bolívares): "
    Leer interesPagado
    tiempo <- 4  // Se establece el tiempo fijo en 4 años
	
    // Cálculo de la tasa de interés anual
    tasaInteres <- (interesPagado * 100) / (capital * tiempo)
	
    // Mostrar resultado
    Escribir "--------------------------------------------------"
    Escribir "La tasa de interés anual cobrada es: ", tasaInteres, " %"
    Escribir "--------------------------------------------------"
FinProceso
