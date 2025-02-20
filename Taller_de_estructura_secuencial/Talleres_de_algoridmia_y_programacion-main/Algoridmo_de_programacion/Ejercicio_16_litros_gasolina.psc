Proceso CalcularPagoGasolina
    Definir galones, litros, precioPorLitro, totalPagar Como Real
    Definir litrosPorGalon Como Real
	
    // Definir la conversión de galones a litros
    litrosPorGalon <- 3.785
    precioPorLitro <- 50000  // Precio del litro de gasolina en COP
	
    // Entrada de datos
    Escribir "Ingrese la cantidad de galones surtidos: "
    Leer galones
	
    // Cálculo de litros y total a pagar
    litros <- galones * litrosPorGalon
    totalPagar <- litros * precioPorLitro
	
    // Mostrar resultado
    Escribir "--------------------------------------------------"
    Escribir "Cantidad de litros surtidos: ", litros, " L"
    Escribir "Total a pagar: ", totalPagar, " COP"
    Escribir "--------------------------------------------------"
FinProceso