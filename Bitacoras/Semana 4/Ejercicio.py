## Ejercicio 5:
from validaciones import validar_correo

validos = 0
invalidos = 0

for i in range(10):
    correo = input(f"Ingrese el correo {i + 1}: ")

    if validar_correo(correo):
        validos += 1
    else:
        invalidos += 1

print("Correos válidos:", validos)
print("Correos inválidos:", invalidos)

##Ejercicio 6:
def clasificar_valor(valor):
    if valor < 60:
        return "BAJO"
    elif valor < 80:
        return "NORMAL"
    else:
        return "ALTO"

bajo = 0
normal = 0
alto = 0

for i in range(10):
    valor = float(input(f"Ingrese el valor {i + 1}: "))

    categoria = clasificar_valor(valor)

    print("Categoría:", categoria)

    if categoria == "BAJO":
        bajo += 1
    elif categoria == "NORMAL":
        normal += 1
    else:
        alto += 1

print("BAJO:", bajo)
print("NORMAL:", normal)
print("ALTO:", alto)

##Ejercicio 7:
from validaciones import validar_nombre

validos = 0
invalidos = 0
total = 8

for i in range(total):
    nombre = input(f"Ingrese el nombre {i + 1}: ")

    if validar_nombre(nombre):
        validos += 1
    else:
        invalidos += 1

porcentaje = (validos / total) * 100

print("Válidos:", validos)
print("Inválidos:", invalidos)
print("Porcentaje de calidad:", porcentaje, "%")

##Ejercicio 8:
from validaciones import validar_rango

validas = 0
invalidas = 0

for i in range(10):
    edad = int(input(f"Ingrese la edad {i + 1}: "))

    if validar_rango(edad, 0, 120):
        validas += 1
    else:
        invalidas += 1

print("Edades válidas:", validas)
print("Edades inválidas:", invalidas)

##Ejercicio 9:
from validaciones import validar_nombre, validar_correo, validar_rango

for i in range(5):

    print(f"Registro {i + 1}")

    nombre = input("Nombre: ")
    correo = input("Correo: ")
    edad = int(input("Edad: "))

    nombre_valido = validar_nombre(nombre)
    correo_valido = validar_correo(correo)
    edad_valida = validar_rango(edad, 0, 120)

    if nombre_valido and correo_valido and edad_valida:
        print("Registro válido")
    else:
        print("Registro inválido")

##Ejercicio 10:
from validaciones import validar_nombre, validar_correo, validar_rango

total = 5
validos = 0
invalidos = 0

for i in range(total):

    print(f"\nRegistro {i + 1}")

    nombre = input("Nombre: ")
    correo = input("Correo: ")
    edad = int(input("Edad: "))
    valor = float(input("Valor: "))

    nombre_valido = validar_nombre(nombre)
    correo_valido = validar_correo(correo)
    edad_valida = validar_rango(edad, 0, 120)
    valor_valido = validar_rango(valor, 0, 100)

    if nombre_valido and correo_valido and edad_valida and valor_valido:
        validos += 1
        print("Registro válido")
    else:
        invalidos += 1
        print("Registro inválido")

print("\nResumen")
print("Total:", total)
print("Válidos:", validos)
print("Inválidos:", invalidos)

##Ejercicio 11:
calidad = (validos / total) * 100
validos = 17
total = 20
calidad = (17 / 20) * 100
calidad = 0.85 * 100
calidad = 85
Calidad de los datos: 85 %
`