usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"}
}
intentos = 3
while intentos > 0:
    usuario_ingresado = input("Ingrese su nombre de usuario: ")
    password_ingresada = input("Ingrese su contraseña: ")

    if usuario_ingresado in usuarios and usuarios[usuario_ingresado]["password"] == password_ingresada:
        print(f"\n¡Acceso concedido!")
        print(f"Bienvenido, {usuarios[usuario_ingresado]['nombre']} {usuarios[usuario_ingresado]['apellido']}.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Credenciales incorrectas. Le quedan {intentos} intentos.")
        else:
            print("\nNúmero máximo de intentos alcanzado. Acceso denegado.")

if intentos == 0:
    print("El programa ha finalizado.")