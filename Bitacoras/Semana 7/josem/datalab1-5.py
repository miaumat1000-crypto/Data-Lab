def mostrar_mensaje():
    print("Bienvenido a DataLab")

mostrar_mensaje()

def saludar(nombre):
    print(f"Hola, {nombre}. Bienvenido a DataLab")

# Pruebas con diferentes individuos
saludar("Ana")
saludar("Carlos")
saludar("María")

def duplicar(valor):
    return valor * 2

print(duplicar(5))
print(duplicar(0))
print(duplicar(10))

def mostrar_resultado(valor):
    print(valor)

def obtener_resultado(valor):
    return valor


res_print = mostrar_resultado(10)
print("Valor guardado de print:", res_print)


res_return = obtener_resultado(20)
print("Valor guardado de return:", res_return + 5)

def clasificar_valor(valor):
    if valor > 70:
        clasificacion = "ALTO"
    elif valor >= 40:
        clasificacion = "NORMAL"
    else:
        clasificacion = "BAJO"
    return clasificacion


print(clasificar_valor(85))  
print(clasificar_valor(50)) 
print(clasificar_valor(20))