Proceso CambioDivisas
    Definir chelines, dracmas, pesetas Como Real
    Definir pesetasDesdeChelines, francosDesdeDracmas, dolaresDesdePesetas, lirasDesdePesetas Como Real
	
    // Conversión de chelines a pesetas
    Escribir "Ingrese la cantidad en chelines austríacos: "
    Leer chelines
    pesetasDesdeChelines <- (chelines * 956.871) / 100
    Escribir chelines, " chelines austríacos equivalen a ", pesetasDesdeChelines, " pesetas."
	
    // Conversión de dracmas a francos franceses
    Escribir "Ingrese la cantidad en dracmas griegos: "
    Leer dracmas
    francosDesdeDracmas <- (dracmas * 88.607) / 100 / 20.110
    Escribir dracmas, " dracmas griegos equivalen a ", francosDesdeDracmas, " francos franceses."
	
    // Conversión de pesetas a dólares y liras italianas
    Escribir "Ingrese la cantidad en pesetas: "
    Leer pesetas
    dolaresDesdePesetas <- pesetas / 122.499
    lirasDesdePesetas <- (pesetas * 100) / 9.289
    Escribir pesetas, " pesetas equivalen a ", dolaresDesdePesetas, " dólares estadounidenses."
    Escribir pesetas, " pesetas equivalen a ", lirasDesdePesetas, " liras italianas."
FinProceso