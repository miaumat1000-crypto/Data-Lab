# Guía de Implementación: Código Python para DataLab v0.5

Esta guía explica la implementación técnica de los ciclos en el Proyecto Integrador DataLab, asegurando que el código sea modular y resistente a errores.

## 1. Implementación del Menú Interactivo

El corazón de la versión 0.5 es el ciclo de control principal.

```python
def main():
    # Estado inicial: El programa debe ejecutarse
    continuar = True 
    
    while continuar:
        print("\n--- DATALAB: SISTEMA DE PROCESAMIENTO ---")
        print("1. Procesar registros (Ciclo FOR)")
        print("2. Validar datos interactivamente (Ciclo WHILE)")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                # Llamada a funcionalidad de procesamiento fijo
                procesar_registros_fijos()
            case "2":
                # Llamada a funcionalidad de validación dinámica
                validar_datos_dinamicos()
            case "3":
                print("Cerrando DataLab...")
                continuar = False # Actualización del estado para terminar
            case _:
                print("Error: Opción no válida. Intente de nuevo.")

def procesar_registros_fijos():
    print("\n--- Modo Procesamiento Fijo ---")
    cantidad = 5 # Ejemplo: procesar 5 registros
    for i in range(1, cantidad + 1):
        print(f"Procesando registro {i} de {cantidad}...")

def validar_datos_dinamicos():
    print("\n--- Modo Validación Dinámica ---")
    # Simulación de do-while para validar una entrada
    while True:
        dato = input("Ingrese un valor numérico (o 'fin' para volver): ")
        if dato.lower() == 'fin':
            break
        if dato.isdigit():
            print(f"Dato {dato} validado correctamente.")
        else:
            print("Error: El dato no es numérico. Intente de nuevo.")

if __name__ == "__main__":
    main()
```

## 2. Análisis Técnico del Código

### El Ciclo de Control (`while continuar`)
Utilizamos una **variable de control** (`continuar`). El ciclo evalúa esta variable antes de cada iteración. Cuando el usuario elige la opción 3, la variable cambia a `False`, rompiendo el ciclo de forma elegante.

### El Procesamiento Fijo (`for i in range`)
En `procesar_registros_fijos`, el ciclo `for` es la herramienta correcta porque el límite (5 registros) está predefinido. No hay riesgo de ciclo infinito aquí.

### La Validación Dinámica (`while True` + `break`)
En `validar_datos_dinamicos`, simulamos un `do-while`. El programa **debe** pedir el dato al menos una vez. El uso de `break` permite salir del ciclo inmediatamente cuando el usuario escribe 'fin', sin esperar a que termine el bloque de código.

## 3. Buenas Prácticas aplicadas
*   **Prevención de Ciclos Infinitos:** Siempre hay una ruta de salida (`continuar = False` o `break`).
*   **Robustez:** El `case _` en el menú evita que el programa se cierre si el usuario ingresa un valor inesperado.
*   **Modularidad:** Cada funcionalidad está en su propia función, facilitando la actualización de DataLab en las próximas semanas.
