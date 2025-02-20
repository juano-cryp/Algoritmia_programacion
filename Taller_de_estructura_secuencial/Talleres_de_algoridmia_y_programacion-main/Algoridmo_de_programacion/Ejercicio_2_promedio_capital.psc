
	Proceso Calcular_Ganancia
		Definir capital, ganancia, total Como Real
		
		Escribir "Ingrese el capital a invertir: "
		Leer capital
		
		ganancia <- capital * 0.02
		total <- capital + ganancia
		
		Escribir "La ganancia después de un mes es: ", ganancia
		Escribir "El total después de un mes es: ", total
FinProceso