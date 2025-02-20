Proceso ConvertirMetrosAPiesYPulgadas
    Definir metros, pulgadasTotales, pies, pulgadasRestantes Como Real
	
    Escribir "Ingrese la cantidad en metros: "
    Leer metros
	
    pulgadasTotales <- metros * 39.27
    pies <- trunc(pulgadasTotales / 12)
    pulgadasRestantes <- pulgadasTotales - (pies * 12)
	
    Escribir "Equivalencia: ", pies, " pies y ", pulgadasRestantes, " pulgadas."
FinProceso