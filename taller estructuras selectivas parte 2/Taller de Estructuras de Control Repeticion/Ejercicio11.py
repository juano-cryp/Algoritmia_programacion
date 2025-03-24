saldo = 1000  
while True:
    # Mostrar el menú
    print("\n--- Menú Cajero Automático ---")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    
    # Solicitar al usuario que elija una opción
    opcion = input("Selecciona una opción (1-4): ")

    # 
    if opcion == "1":
        # Opción 1: Depositar dinero
        monto = float(input("¿Cuánto dinero deseas depositar? $"))
        if monto > 0:
            saldo += monto
            print(f"Has depositado ${monto}. Tu saldo actual es ${saldo}.")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    elif opcion == "2":
        # Opción 2: Retirar dinero
        monto = float(input("¿Cuánto dinero deseas retirar? $"))
        if monto > 0:
            if monto <= saldo:
                saldo -= monto
                print(f"Has retirado ${monto}. Tu saldo actual es ${saldo}.")
            else:
                print("No tienes suficiente saldo para realizar este retiro.")
        else:
            print("El monto a retirar debe ser mayor que 0.")

    elif opcion == "3":
        # Opción 3: Consultar saldo
        print(f"Tu saldo actual es ${saldo}.")

    elif opcion == "4":
        # Opción 4: Salir
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break  # Sale del ciclo y termina el programa.

    else:
        # Si la opción ingresada no es válida
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")
