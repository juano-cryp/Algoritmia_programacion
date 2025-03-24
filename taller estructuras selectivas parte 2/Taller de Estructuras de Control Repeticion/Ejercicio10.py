numero = int(input("Introduce un número entero positivo: "))
suma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:  # Si i es divisor de numero
        suma_divisores += i  # Agregar el divisor a la suma
if suma_divisores == numero:
    # Si la suma es igual al número, es un número perfecto
    print(f"{numero} es un número perfecto.")
else:
    # Si la suma no es igual, no es un número perfecto
    print(f"{numero} no es un número perfecto.")
