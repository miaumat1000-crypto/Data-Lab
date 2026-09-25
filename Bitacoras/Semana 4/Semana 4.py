
def validar_nombre(nombre):
    nombre = nombre.strip()
    if not nombre:
        return False
    return nombre.replace(" ", "").isalpha()

def validar_correo(correo):
    correo = correo.strip()
    if not correo:
        return False
    return "@" in correo and "." in correo

def validar_rango(valor, minimo, maximo):
    return minimo <= valor <= maximo


def main():
    print("    DATALAB - PROCESAMIENTO DE DATOS    ")

    cantidad = int(input("¿Cuántos registros desea procesar? "))

    validos = 0
    invalidos = 0
    reprobados = 0
    estandar = 0
    excelentes = 0

    for i in range(cantidad):
        print(f"\n--- Registro {i + 1} de {cantidad} ---")

        nombre = input("Ingrese el nombre del estudiante: ")
        correo = input("Ingrese el correo institucional: ")
        edad = int(input("Ingrese la edad: "))
        nota = float(input("Ingrese la nota final (0.0 a 5.0): "))

        nombre_valido = validar_nombre(nombre)
        correo_valido = validar_correo(correo)
        edad_valida = validar_rango(edad, 0, 120)
        nota_valida = validar_rango(nota, 0.0, 5.0)

        if nombre_valido and correo_valido and edad_valida and nota_valida:
            validos += 1
            print("Status: Registro VÁLIDO")

            if nota < 3.0:
                reprobados += 1
                print("Clasificación: El estudiante ha reprobado la materia")
            elif nota < 4.8:
                estandar += 1
                print("Clasificación: El estudiante ha aprobado con una nota estándar")
            else:
                excelentes += 1
                print("Clasificación: El estudiante ha aprobado con la máxima calificación")
        else:
            invalidos += 1
            print("Status: Registro INVÁLIDO (Estructura de datos errónea)")

    calidad = (validos / cantidad) * 100 if cantidad > 0 else 0

    print("    RESUMEN DE CALIDAD DE DATALAB       ")
    print(f"Total de registros procesados : {cantidad}")
    print(f"Registros válidos            : {validos}")
    print(f"Registros inválidos          : {invalidos}")
    print(f"Porcentaje de calidad        : {calidad:.2f}%")
    print("----------------------------------------")
    print("Desglose Académico de Registros Válidos:")
    print(f" - Reprobados (< 3.0)        : {reprobados}")
    print(f" - Nota Estándar (3.0 - 4.79): {estandar}")
    print(f" - Máxima Nota (4.8 - 5.0)   : {excelentes}")

if __name__ == "__main__":
    main()



