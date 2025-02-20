Proceso Calcular_TotalCompra
    Definir totalCompra, descuento, totalPagar Como Real
    
    Escribir "Ingrese el total de la compra: "
    Leer totalCompra
    
    descuento <- totalCompra * 0.15
    totalPagar <- totalCompra - descuento
    
    Escribir "El descuento aplicado es: ", descuento
    Escribir "El total a pagar después del descuento es: ", totalPagar
FinProceso