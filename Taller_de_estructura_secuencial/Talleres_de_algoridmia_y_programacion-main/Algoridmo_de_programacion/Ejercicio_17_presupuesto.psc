Proceso CalcularPresupuestoHospital
    Definir presupuestoTotal, ginecologia, pediatria, traumatologia Como Real
	
    // Entrada de datos
    Escribir "Ingrese el presupuesto total del hospital: "
    Leer presupuestoTotal
	
    // Cálculo de la distribución del presupuesto
    ginecologia <- presupuestoTotal * 0.40
    traumatologia <- presupuestoTotal * 0.30
    pediatria <- presupuestoTotal * 0.30
	
    // Mostrar resultados
    Escribir "--------------------------------------------------"
    Escribir "Presupuesto asignado a cada área:"
    Escribir "Ginecología: ", ginecologia, " COP"
    Escribir "Traumatología: ", traumatologia, " COP"
    Escribir "Pediatría: ", pediatria, " COP"
    Escribir "--------------------------------------------------"
FinProceso
