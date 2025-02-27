from datetime import datetime

def obtener_signo_zodiaco(dia, mes):
    signos = [
        ("Capricornio", (22, 12), (20, 1)),
        ("Acuario", (21, 1), (19, 2)),
        ("Piscis", (20, 2), (19, 3)),
        ("Aries", (21, 3), (20, 4)),
        ("Tauro", (21, 4), (21, 5)),
        ("Géminis", (22, 5), (21, 6)),
        ("Cáncer", (22, 6), (22, 7)),
        ("Leo", (23, 7), (23, 8)),
        ("Virgo", (24, 8), (22, 9)),
        ("Libra", (23, 9), (22, 10)),
        ("Escorpión", (23, 10), (21, 11)),
        ("Sagitario", (22, 11), (21, 12))
    ]

    for signo, (dia_inicio, mes_inicio), (dia_fin, mes_fin) in signos:
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            return signo
    return "Desconocido"

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    fecha_nac = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
    return edad

# Entrada del usuario
fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
dia, mes, anio = map(int, fecha_nacimiento.split("/"))

# Cálculo del signo zodiacal y la edad
signo = obtener_signo_zodiaco(dia, mes)
edad = calcular_edad(fecha_nacimiento)

# Mostrar resultados
print(f"Su signo zodiacal es: {signo}")
print(f"Su edad es: {edad} años")