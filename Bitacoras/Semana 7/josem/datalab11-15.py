def ejecutar_operacion_uno():
    print("Ejecutando la operación 1...")

def ejecutar_operacion_dos():
    print("Ejecutando la operación 2...")

def ejecutar_operacion_tres():
    print("Ejecutando la operación 3...")

def procesar_registros(cantidad):
    contador = 0
    acumulador = 0
    bandera = False
    
    contador_altos = 0
    contador_normales = 0
    
    for i in range(cantidad):
        print(f"\n--- Procesando registro {i + 1} de {cantidad} ---")
        valor = float(input("Ingrese el valor numérico del registro: "))
        contador += 1
        acumulador += valor
        
        if valor > 10:
            bandera = True
            contador_altos += 1  
            print("Clasificación: Valor alto detectado.")
        else:
            contador_normales += 1  
            print("Clasificación: Valor estándar.")

    
    resultado = {
        "total_registros": contador,
        "suma_acumulada": acumulador,
        "bandera_activa": bandera,
        "altos": contador_altos,
        "normales": contador_normales
    }
    return resultado

def mostrar_resumen(total, altos, normales, bajos, suma, existe_alto):
    print("\n" + "="*30)
    print("       RESUMEN DE REGISTROS     ")
    print("="*30)
    print(f"Total de registros procesados : {total}")
    print(f"Suma acumulada de valores     : {suma}")
    print(f"Registros altos               : {altos}")
    print(f"Registros normales            : {normales}")
    print(f"Registros bajos               : {bajos}")
    
    if existe_alto:
        print("Alerta: ¡Se detectaron valores altos en el proceso! (Bandera activa)")
    else:
        print("Estado: Todos los valores se mantuvieron en niveles estándar o bajos.")
    print("="*30)

def ejecutar_opcion(opcion):
    if opcion == 1:
        cant = int(input("Ingrese la cantidad de registros a procesar: "))
        resultado = procesar_registros(cant)
        
        
        mostrar_resumen(
            total=resultado["total_registros"],
            altos=resultado["altos"],         
            normales=resultado["normales"],   
            bajos=0,                          
            suma=resultado["suma_acumulada"],
            existe_alto=resultado["bandera_activa"]
        )
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

