def calcular_costo_alquiler(distancia_km):
    if distancia_km <= 300:
        return 50000  # Caso a: hasta 300 km
    elif distancia_km <= 1000:
        km_extra = distancia_km - 300
        return 70000 + (30000 * km_extra)  # Caso b.i: entre 301 y 1000 km
    else:
        km_extra = distancia_km - 1000
        return 150000 + (9000 * km_extra)  # Caso b.ii: más de 1000 km

# Entrada del usuario
distancia = float(input("Ingrese la distancia recorrida en km: "))

# Cálculo del costo
costo_total = calcular_costo_alquiler(distancia)

# Mostrar resultado
print(f"El total a pagar por el alquiler es: {costo_total:,} COP")
