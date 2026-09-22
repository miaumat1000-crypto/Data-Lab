import validaciones_basicas as vb
#from validaciones_basicas import validar_nombre

# Ejercicio 1:
for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")

    if vb.validar_nombre(nombre):
        print("Nombre válido")
    else:
        print("Nombre inválido")


#Ejercicio 2:
for i in range(5):
    correo = input(f"Ingrese el correo {i + 1}: ")

    if vb.validar_correo(correo):
        print("Correo válido")
    else:
        print("Correo inválido")

#Ejercicio 3:
for i in range(5):
    valor = float(input(f"Ingrese el valor {i + 1}: "))

    if vb.validar_rango(valor, 0, 100):
        print("Valor válido")
    else:
        print("Valor fuera del rango")

#Ejercicio 4:
for i in range(5):
    opcion = int(input("Seleccione una opción (1, 2 o 3): "))

    if vb.validar_opcion(opcion):
        print("Opción válida")
    else:
        print("Opción inválida")

#Ejercicio 5:
validos = 0
invalidos = 0

for i in range(10):
    correo = input(f"Ingrese el correo {i + 1}: ")

    if vb.validar_correo(correo):
        validos += 1
    else:
        invalidos += 1

print("Correos válidos:", validos)
print("Correos inválidos:", invalidos)

#Ejercicio 6
bajo = 0
normal = 0
alto = 0

for i in range(10):
    valor = float(input(f"Ingrese el valor {i + 1}: "))

    categoria = vb.clasificar_valor(valor)

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

#Ejercicio 7: 
validos = 0
invalidos = 0
total = 8

for i in range(total):
    nombre = input(f"Ingrese el nombre {i + 1}: ")

    if vb.validar_nombre(nombre):
        validos += 1
    else:
        invalidos += 1

porcentaje = (validos / total) * 100

print("Válidos:", validos)
print("Inválidos:", invalidos)
print("Porcentaje de calidad:", porcentaje, "%")

#Ejercicio 8:


validas = 0
invalidas = 0

for i in range(10):
    edad = int(input(f"Ingrese la edad {i + 1}: "))

    if vb.validar_rango(edad, 0, 120):
        validas += 1
    else:
        invalidas += 1

print("Edades válidas:", validas)
print("Edades inválidas:", invalidas)

#Ejercicio 9:
for i in range(5):

    print(f"Registro {i + 1}")

    nombre = input("Nombre: ")
    correo = input("Correo: ")
    edad = int(input("Edad: "))

    nombre_valido = vb.validar_nombre(nombre)
    correo_valido = vb.validar_correo(correo)
    edad_valida = vb.validar_rango(edad, 0, 120)

    if nombre_valido and correo_valido and edad_valida:
        print("Registro válido")
    else:
        print("Registro inválido")

#Ejercicio 10
total = 5
validos = 0
invalidos = 0

for i in range(total):

    print(f"\nRegistro {i + 1}")

    nombre = input("Nombre: ")
    correo = input("Correo: ")
    edad = int(input("Edad: "))
    valor = float(input("Valor: "))

    nombre_valido = vb.validar_nombre(nombre)
    correo_valido = vb.validar_correo(correo)
    edad_valida = vb.validar_rango(edad, 0, 120)
    valor_valido = vb.validar_rango(valor, 0, 100)

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


