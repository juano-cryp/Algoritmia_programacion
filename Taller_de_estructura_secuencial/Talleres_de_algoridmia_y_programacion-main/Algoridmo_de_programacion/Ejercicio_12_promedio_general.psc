Proceso CalcularPromedios
    Definir examenMat, tareaMat1, tareaMat2, tareaMat3, promTareasMat, promedioMat Como Real
    Definir examenFis, tareaFis1, tareaFis2, promTareasFis, promedioFis Como Real
    Definir examenQuim, tareaQuim1, tareaQuim2, tareaQuim3, promTareasQuim, promedioQuim Como Real
    Definir promedioGeneral Como Real
	
    // Entrada de datos para Matemática
    Escribir "Ingrese la nota del examen de Matemática: "
    Leer examenMat
    Escribir "Ingrese la nota de la primera tarea de Matemática: "
    Leer tareaMat1
    Escribir "Ingrese la nota de la segunda tarea de Matemática: "
    Leer tareaMat2
    Escribir "Ingrese la nota de la tercera tarea de Matemática: "
    Leer tareaMat3
	
    // Cálculo del promedio de Matemática
    promTareasMat <- (tareaMat1 + tareaMat2 + tareaMat3) / 3
    promedioMat <- (examenMat * 0.90) + (promTareasMat * 0.10)
	
    // Entrada de datos para Física
    Escribir "Ingrese la nota del examen de Física: "
    Leer examenFis
    Escribir "Ingrese la nota de la primera tarea de Física: "
    Leer tareaFis1
    Escribir "Ingrese la nota de la segunda tarea de Física: "
    Leer tareaFis2
	
    // Cálculo del promedio de Física
    promTareasFis <- (tareaFis1 + tareaFis2) / 2
    promedioFis <- (examenFis * 0.80) + (promTareasFis * 0.20)
	
    // Entrada de datos para Química
    Escribir "Ingrese la nota del examen de Química: "
    Leer examenQuim
    Escribir "Ingrese la nota de la primera tarea de Química: "
    Leer tareaQuim1
    Escribir "Ingrese la nota de la segunda tarea de Química: "
    Leer tareaQuim2
    Escribir "Ingrese la nota de la tercera tarea de Química: "
    Leer tareaQuim3
	
    // Cálculo del promedio de Química
    promTareasQuim <- (tareaQuim1 + tareaQuim2 + tareaQuim3) / 3
    promedioQuim <- (examenQuim * 0.85) + (promTareasQuim * 0.15)
	
    // Cálculo del promedio general
    promedioGeneral <- (promedioMat + promedioFis + promedioQuim) / 3
	
    // Mostrar resultados
    Escribir "--------------------------------------------------"
    Escribir "Promedio en Matemática: ", promedioMat
    Escribir "Promedio en Física: ", promedioFis
    Escribir "Promedio en Química: ", promedioQuim
    Escribir "--------------------------------------------------"
    Escribir "Promedio general en las tres materias: ", promedioGeneral
    Escribir "--------------------------------------------------"
FinProceso