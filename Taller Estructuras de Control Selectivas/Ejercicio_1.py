def calcular_inversion_final(monto_inicial, tasa_interes, años):
    saldo = monto_inicial
    for año in range(1, años + 1):
        # Calcular el interés generado en el año
        interes = saldo * tasa_interes
        print(f"Año {año}: Intereses generados = {interes:.2f} COP")
        
        # Verificar si los intereses exceden $100,000 COP
        if interes > 100000:
            print(f"Intereses exceden los $100,000 COP. Reinvirtiendo los intereses.")
            saldo += interes  # Reinvertir los intereses
        else:
            print(f"Intereses menores a $100,000 COP. No se reinvierten.")
        
    return saldo

# Datos de entrada
monto_inicial = float(input("Ingrese el monto inicial de la inversión en COP: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje, por ejemplo 5 para 5%): ")) / 100
años = int(input("Ingrese el número de años que durará la inversión: "))

# Llamada a la función
saldo_final = calcular_inversion_final(monto_inicial, tasa_interes, años)

# Mostrar el saldo final
print(f"El saldo final en la cuenta después de {años} años es: {saldo_final:.2f} COP")

