Proceso Calcular_SalarioNeto
    Definir horasTrabajadas, precioHora, salarioBruto, descuento, salarioNeto Como Real
	
    Escribir "Ingrese el número de horas trabajadas: "
    Leer horasTrabajadas
	
    Escribir "Ingrese el precio por hora trabajada: "
    Leer precioHora
	
    salarioBruto <- horasTrabajadas * precioHora
    descuento <- salarioBruto * 0.20
    salarioNeto <- salarioBruto - descuento
	
    Escribir "El salario bruto es: ", salarioBruto
    Escribir "El descuento por impuestos es: ", descuento
    Escribir "El salario neto a recibir es: ", salarioNeto
FinProceso