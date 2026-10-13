def clasificar_valor(valor):
    if valor > 60.0:
        return "Alto"
    elif valor >= 40.0:
        return "Normal"
    else:
        return "Bajo"

def ejecutar_prueba(nombre_caso, valores):
    total_registros = 0
    contador_altos = 0
    contador_normales = 0
    contador_bajos = 0
    suma_valores = 0.0
    existe_alto = False

    for valor in valores:
        total_registros += 1
        suma_valores += valor
        clasificacion = clasificar_valor(valor)
        
        if clasificacion == "Alto":
            contador_altos += 1
            existe_alto = True
        elif clasificacion == "Normal":
            contador_normales += 1
        elif clasificacion == "Bajo":
            contador_bajos += 1

    print(f"--- {nombre_caso} ---")
    print(f"Datos: {valores}")
    print(f"Resultados Total: {total_registros}")
    print(f"Alto: {contador_altos}")
    print(f"Normal: {contador_normales}")
    print(f"Bajo: {contador_bajos}")
    print(f"Suma: {suma_valores}")
    print(f"Existe ALTO: {existe_alto}\n")
          
# Ejecución de los 6 casos de prueba
ejecutar_prueba("Caso 1: Todos NORMAL", [45.0, 50.0, 55.0])
ejecutar_prueba("Caso 2: Un ALTO", [45.0, 75.0, 50.0])
ejecutar_prueba("Caso 3: Varios ALTO", [65.0, 80.0, 45.0])
ejecutar_prueba("Caso 4: Todos BAJO", [10.0, 20.0, 30.0])
ejecutar_prueba("Caso 5: Datos mixtos", [22.5, 55.1, 72.3, 38.7, 61.4])
ejecutar_prueba("Caso 6: Datos conocidos", [10, 20, 30, 40, 50])