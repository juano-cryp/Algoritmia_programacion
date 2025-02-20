Proceso Calcular_SueldoVendedor
    Definir sueldoBase, venta1, venta2, venta3, comisiones, sueldoTotal Como Real
    
    Escribir "Ingrese el sueldo base del vendedor: "
    Leer sueldoBase
    
    Escribir "Ingrese el monto de la primera venta: "
    Leer venta1
    
    Escribir "Ingrese el monto de la segunda venta: "
    Leer venta2
    
    Escribir "Ingrese el monto de la tercera venta: "
    Leer venta3
    
    comisiones <- (venta1 + venta2 + venta3) * 0.10
    sueldoTotal <- sueldoBase + comisiones
    
    Escribir "El total de comisiones es: ", comisiones
    Escribir "El sueldo total del vendedor es: ", sueldoTotal
FinProceso