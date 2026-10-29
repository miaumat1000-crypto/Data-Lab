def clasificar_valor(valor):
    # Ajusta estos rangos según las reglas de tu Dataset de Trabajo / DataLab
    if valor > 60:
        clasificacion = "ALTO"
    elif valor >= 40:
        clasificacion = "NORMAL"
    else:
        clasificacion = "BAJO"
    return clasificacion
# Reto 6 

def contar_registros(valores):
    contador = 0
    for valor in valores:
        contador += 1
    return contador 

# Prueba:
print(contar_registros([22, 55, 72, 38, 61]))  

# Resultado: 5

# Reto 7

def calcular_suma(valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma

# Prueba:
print(calcular_suma([10, 20, 30, 40]))  

# Resultado: 100

# Reto 8
def procesar_resumen_categorias(valores):
    altos = 0
    normales = 0
    bajos = 0
    for valor in valores:
        categoria = clasificar_valor(valor)
        if categoria == "ALTO":
            altos += 1
        elif categoria == "NORMAL":
            normales += 1
        elif categoria == "BAJO":
            bajos += 1
    return altos, normales, bajos

# Reto 9 
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Procesar registros")
    print("2. Ver resumen y estadísticas")
    print("3. Salir")

# Reto 10
def leer_opción():
    opción = input("Por favor, seleccione una opción: ☺︎")
    return opción      
