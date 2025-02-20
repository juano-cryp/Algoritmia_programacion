Proceso CalcularPagoLuz
    Definir lecturaAnterior, lecturaActual, costoPorKilovatio, consumo, montoTotal Como Real
	
    // Entrada de datos
    Escribir "Ingrese la lectura anterior del medidor (kWh): "
    Leer lecturaAnterior
    Escribir "Ingrese la lectura actual del medidor (kWh): "
    Leer lecturaActual
    Escribir "Ingrese el costo por kilovatio (COP/kWh): "
    Leer costoPorKilovatio
	
    // Cálculo del consumo
    consumo <- lecturaActual - lecturaAnterior
    montoTotal <- consumo * costoPorKilovatio
	
    // Mostrar resultado
    Escribir "--------------------------------------------------"
    Escribir "Consumo de energía en el mes: ", consumo, " kWh"
    Escribir "Monto total a pagar: ", montoTotal, " COP"
    Escribir "--------------------------------------------------"
FinProceso

