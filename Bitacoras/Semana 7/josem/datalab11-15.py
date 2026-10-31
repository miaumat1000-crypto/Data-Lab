def mostrar_menu():
    print("\n--- ♫ MENÚ PRINCIPAL ♫ ---")
    print("1. Procesar registros y mostrar resumen")
    print("2. Ejecutar operación 2")
    print("3. Ejecutar operación 3")
    print("4. Salir")

def leer_opcion():
    try:
        return int(input("Por favor, digite una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 0  

def clasificar_valor(valor):
    if valor > 10:
        print("Clasificación: Valor alto detectado.")
        return "alto"
    else:
        print("Clasificación: Valor estándar.")
        return "normal"

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
        
        
        clasificacion = clasificar_valor(valor)
        if clasificacion == "alto":
            bandera = True
            contador_altos += 1
        else:
            contador_normales += 1

    return {
        "total_registros": contador,
        "suma_acumulada": acumulador,
        "bandera_activa": bandera,
        "altos": contador_altos,
        "normales": contador_normales
    }

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
        print("Alerta: Se detectaron valores altos en el proceso.")
    else:
        print("Estado: Todos los valores se mantuvieron en niveles estándar.")
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
    elif opcion == 2:
        print("Ejecutando operación 2...")
    elif opcion == 3:
        print("Ejecutando operación 3...")
    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    opcion = 0
    while opcion != 4:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion != 4:
            ejecutar_opcion(opcion)

