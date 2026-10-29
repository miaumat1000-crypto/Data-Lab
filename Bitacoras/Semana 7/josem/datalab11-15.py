def ejecutar_operacion_uno():
    print("Ejecutando la operación 1...")

def ejecutar_operacion_dos():
    print("Ejecutando la operación 2...")

def ejecutar_operacion_tres():
    print("Ejecutando la operación 3...")

def ejecutar_opcion(opcion):
    if opcion == 1:
        ejecutar_operacion_uno()
    elif opcion == 2:
        ejecutar_operacion_dos()
    elif opcion == 3:
        ejecutar_operacion_tres()
    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
if __name__ == "__main__":
    opcion = 0
    while opcion != 4:
        print("\n---♬ MENÚ PRINCIPAL ♪---")
        print("1. Ejecutar operación 1")
        print("2. Ejecutar operación 2")
        print("3. Ejecutar operación 3")
        print("4. Salir")
        
        try:
            opcion = int(input("Por favor, digite una opción: "))
            ejecutar_opcion(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")