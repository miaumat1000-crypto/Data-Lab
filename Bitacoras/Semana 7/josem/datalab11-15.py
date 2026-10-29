def ejecutar_operacion_uno():
    print("Ejecutando la operación 1...")

def ejecutar_operacion_dos():
    print("Ejecutando la operación 2...")

def ejecutar_operacion_tres():
    print("Ejecutando la operación 3...")

def procesar_registros(cantidad):
    """
    Procesa los registros de manera independiente a la lógica del menú,
    utilizando contadores, acumuladores, clasificación y banderas.
    """
    contador = 0
    acumulador = 0
    bandera = False  
    
    for i in range(cantidad):
        print(f"\n--- Procesando registro {i + 1} de {cantidad} ---")
        
        
        # Ejemplo numérico:
        valor = float(input("Ingrese el valor numérico del registro: "))
        
        
        contador += 1
        acumulador += valor
        
        
        if valor > 10:  
            bandera = True
            print("Clasificación: Valor alto detectado.")
        else:
            print("Clasificación: Valor estándar.")
    resultado = {
        "total_registros": contador,
        "suma_acumulada": acumulador,
        "bandera_activa": bandera
    }
    return resultado

def ejecutar_opcion(opcion):
    if opcion == 1:
        
        cant = int(input("Ingrese la cantidad de registros a procesar: "))
        resultado = procesar_registros(cant)
        print("Resultado obtenido:", resultado)
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
        print("\n---♬  MENÚ PRINCIPAL ♪---")
        print("1. Procesar registros")
        print("2. Ejecutar operación 2")
        print("3. Ejecutar operación 3")
        print("4. Salir")
        
        try:
            opcion = int(input("Por favor, digite una opción: "))
            
            ejecutar_opcion(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

