"""
validaciones_basicas.py

Material de apoyo - Lógica Computacional
Semana 04 - Ciclos for y range()

Propósito
---------
Este archivo contiene validaciones básicas que pueden reutilizarse
cuando se procesan diferentes datasets.

La idea es que los estudiantes:
1. Entiendan la lógica de cada validación.
2. Reutilicen las funciones en lugar de copiar código.
3. Amplíen las funciones cuando aparezcan nuevas necesidades.
4. Combinen estas funciones con ciclos for para procesar múltiples registros.

IMPORTANTE
----------
No se utilizan librerías externas. Solamente:
- if / elif / else
- match / case
- funciones
- expresiones regulares mediante el módulo estándar re
- operaciones básicas de cadenas y números
"""

import re


# ============================================================
# 1. VALIDACIONES BÁSICAS DE TEXTO
# ============================================================

def validar_cadena_no_vacia(texto):
    """
    Verifica que una cadena tenga contenido.

    strip() elimina espacios al inicio y al final.
    """
    if texto is None:
        return False

    return texto.strip() != ""


def validar_longitud(texto, minimo, maximo):
    """
    Verifica que la longitud de una cadena esté dentro de un rango.

    Ejemplo:
        validar_longitud("Python", 3, 10) -> True
    """
    if texto is None:
        return False

    longitud = len(texto.strip())

    return minimo <= longitud <= maximo


# ============================================================
# 2. EXPRESIONES REGULARES
# ============================================================

"""
¿Qué es una expresión regular?

Una expresión regular, o REGEX, es una forma de describir un patrón
que debe cumplir un texto.

Ejemplos sencillos:

    ^texto$
    ^[0-9]+$
    ^[A-Za-z]+$

Algunos símbolos importantes:

    ^       Inicio del texto
    $       Final del texto
    []      Conjunto de caracteres permitidos
    +       Uno o más caracteres
    ?       Cero o un carácter
    \\d      Un dígito
    \\s      Un espacio
    \\w      Letra, número o "_"
    .       Cualquier carácter (en muchos patrones)

En este material utilizamos expresiones regulares sencillas.
El objetivo es comprender el concepto, no memorizar patrones complejos.
"""


# ============================================================
# 3. CORREO ELECTRÓNICO
# ============================================================

def validar_correo(correo):
    """
    Validación básica de correo electrónico.

    Ejemplos válidos:
        usuario@gmail.com
        nombre.apellido@universidad.edu.co

    Ejemplos inválidos:
        usuario
        usuario@
        @gmail.com
        usuario@gmail
    """

    if not validar_cadena_no_vacia(correo):
        return False

    patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.match(patron, correo.strip()) is not None


# ============================================================
# 4. NOMBRES DE PERSONAS
# ============================================================

def validar_nombre(nombre):
    """
    Verifica que un nombre contenga solamente letras y espacios.

    Se incluyen letras con tildes y Ñ propias del español.

    Ejemplos válidos:
        Ana
        Juan Pérez
        María José
        José Rodríguez

    Ejemplos inválidos:
        Juan123
        Ana_123
        4567
    """

    if not validar_cadena_no_vacia(nombre):
        return False

    patron = (
        r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+"
        r"( [A-Za-zÁÉÍÓÚáéíóúÑñÜü]+)*$"
    )

    return re.match(patron, nombre.strip()) is not None


# ============================================================
# 5. TELÉFONO CELULAR
# ============================================================

def validar_celular(celular):
    """
    Validación básica para números de celular colombianos.

    Se espera:
        - 10 dígitos
        - comenzar por 3

    Ejemplos:
        3001234567 -> válido
        3159876543 -> válido
        1234567890 -> inválido
        300123456  -> inválido

    Esta es una validación de formato, no verifica que el número
    exista realmente.
    """

    if not validar_cadena_no_vacia(celular):
        return False

    patron = r"^3\d{9}$"

    return re.match(patron, celular.strip()) is not None


# ============================================================
# 6. VALORES NUMÉRICOS DENTRO DE UN RANGO
# ============================================================

def validar_rango(valor, minimo, maximo):
    """
    Verifica que un número esté entre un mínimo y un máximo,
    incluyendo ambos límites.

    Ejemplo:
        validar_rango(80, 0, 100) -> True
    """
    return minimo <= valor <= maximo


# ============================================================
# 7. EDAD
# ============================================================

def validar_edad(edad):
    """
    Edad básica entre 0 y 120 años.
    """
    return validar_rango(edad, 0, 120)


# ============================================================
# 8. NOTA ACADÉMICA
# ============================================================

def validar_nota(nota):
    """
    Valida una nota académica en escala de 0.0 a 5.0.
    """
    return validar_rango(nota, 0.0, 5.0)


# ============================================================
# 9. DOCUMENTO NUMÉRICO
# ============================================================

def validar_documento(documento):
    """
    Verifica que un documento contenga únicamente números.

    También exige una longitud entre 6 y 12 dígitos.
    """

    if not validar_cadena_no_vacia(documento):
        return False

    patron = r"^\d{6,12}$"

    return re.match(patron, documento.strip()) is not None


# ============================================================
# 10. CÓDIGO DE PRODUCTO
# ============================================================

def validar_codigo_producto(codigo):
    """
    Ejemplo de código de producto:

        ABC123
        PROD001

    Regla:
        - Letras mayúsculas
        - Seguidas de números
        - Entre 2 y 6 letras
        - Entre 2 y 6 números
    """

    if not validar_cadena_no_vacia(codigo):
        return False

    patron = r"^[A-Z]{2,6}[0-9]{2,6}$"

    return re.match(patron, codigo.strip()) is not None


# ============================================================
# 11. VALORES PERMITIDOS
# ============================================================

def validar_valor_permitido(valor, valores_permitidos):
    """
    Verifica si un valor pertenece a una lista de opciones.

    Ejemplo:
        validar_valor_permitido(
            "ACTIVO",
            ["ACTIVO", "INACTIVO"]
        )
    """

    return valor in valores_permitidos


# ============================================================
# 12. RESPUESTA SÍ / NO
# ============================================================

def validar_si_no(respuesta):
    """
    Permite solamente:
        SI
        NO

    Se convierte a mayúsculas para aceptar:
        si
        Si
        sI
        SI
    """

    if not validar_cadena_no_vacia(respuesta):
        return False

    respuesta = respuesta.strip().upper()

    return respuesta == "SI" or respuesta == "NO"


# ============================================================
# 13. MATCH - NIVEL DE ESCOLARIDAD
# ============================================================

def nivel_escolaridad(codigo):
    """
    Utiliza match para convertir un código numérico
    en una descripción.

    0 - Sin estudio
    1 - Primaria
    2 - Secundaria
    3 - Técnico/Tecnólogo
    4 - Universitario
    5 - Posgrado
    """

    match codigo:
        case 0:
            return "Sin estudio"
        case 1:
            return "Primaria"
        case 2:
            return "Secundaria"
        case 3:
            return "Técnico/Tecnólogo"
        case 4:
            return "Universitario"
        case 5:
            return "Posgrado"
        case _:
            return "Código no válido"


# ============================================================
# 14. MATCH - ESTADO DE UN REGISTRO
# ============================================================

def estado_registro(codigo):
    """
    Convierte un código de estado en una descripción.

    1 - Activo
    2 - Inactivo
    3 - Pendiente
    4 - Bloqueado
    """

    match codigo:
        case 1:
            return "Activo"
        case 2:
            return "Inactivo"
        case 3:
            return "Pendiente"
        case 4:
            return "Bloqueado"
        case _:
            return "Estado no válido"


# ============================================================
# 15. MATCH - TIPO DE DOCUMENTO
# ============================================================

def tipo_documento(codigo):
    """
    Clasifica un tipo de documento.

    1 - Cédula de ciudadanía
    2 - Tarjeta de identidad
    3 - Cédula de extranjería
    4 - Pasaporte
    """

    match codigo:
        case 1:
            return "Cédula de ciudadanía"
        case 2:
            return "Tarjeta de identidad"
        case 3:
            return "Cédula de extranjería"
        case 4:
            return "Pasaporte"
        case _:
            return "Tipo de documento no válido"


# ============================================================
# 16. MATCH - TIPO DE USUARIO
# ============================================================

def tipo_usuario(codigo):
    """
    Clasifica el tipo de usuario.

    1 - Estudiante
    2 - Docente
    3 - Administrativo
    4 - Externo
    """

    match codigo:
        case 1:
            return "Estudiante"
        case 2:
            return "Docente"
        case 3:
            return "Administrativo"
        case 4:
            return "Externo"
        case _:
            return "Tipo de usuario no válido"


# ============================================================
# 17. MATCH - ESTADO CIVIL
# ============================================================

def estado_civil(codigo):
    """
    1 - Soltero(a)
    2 - Casado(a)
    3 - Unión libre
    4 - Separado(a)
    5 - Divorciado(a)
    6 - Viudo(a)
    """

    match codigo:
        case 1:
            return "Soltero(a)"
        case 2:
            return "Casado(a)"
        case 3:
            return "Unión libre"
        case 4:
            return "Separado(a)"
        case 5:
            return "Divorciado(a)"
        case 6:
            return "Viudo(a)"
        case _:
            return "Estado civil no válido"


# ============================================================
# 18. MATCH - CLASIFICACIÓN DE UN VALOR
# ============================================================

def clasificar_valor(categoria):
    """
    Ejemplo de selección mediante match.

    1 - Bajo
    2 - Normal
    3 - Alto
    """

    match categoria:
        case 1:
            return "Bajo"
        case 2:
            return "Normal"
        case 3:
            return "Alto"
        case _:
            return "Categoría no válida"


# ============================================================
# 19. EJEMPLO DE USO CON IF / ELSE
# ============================================================

def ejemplo_if_else():
    """
    Ejemplo sencillo de cómo utilizar una validación.
    """

    correo = input("Ingrese un correo: ")

    if validar_correo(correo):
        print("Correo válido")
    else:
        print("Correo inválido")


# ============================================================
# 20. EJEMPLO DE USO CON MATCH
# ============================================================

def ejemplo_match():
    """
    Ejemplo sencillo de utilización de match-case.
    """

    codigo = int(input("Ingrese el código de escolaridad: "))

    resultado = nivel_escolaridad(codigo)

    print("Nivel:", resultado)


# ============================================================
# 21. EJEMPLO PARA PROCESAR VARIOS DATOS
# ============================================================

def ejemplo_procesamiento():
    """
    Este ejemplo muestra cómo reutilizar una misma función
    dentro de un ciclo.

    En la Semana 04 esta idea será fundamental:
    una validación se programa una vez y se reutiliza
    para muchos datos.
    """

    correos = [
        "ana@gmail.com",
        "correo-invalido",
        "juan@universidad.edu.co",
        "usuario@",
        "maria@hotmail.com"
    ]

    validos = 0
    invalidos = 0

    for correo in correos:

        if validar_correo(correo):
            validos += 1
            print(correo, "-> válido")
        else:
            invalidos += 1
            print(correo, "-> inválido")

    print()
    print("Total válidos:", validos)
    print("Total inválidos:", invalidos)


# ============================================================
# 22. EJEMPLO DE REGISTRO
# ============================================================

def validar_registro(nombre, correo, edad, celular):
    """
    Un registro es válido si todos sus campos cumplen
    las reglas correspondientes.
    """

    nombre_ok = validar_nombre(nombre)
    correo_ok = validar_correo(correo)
    edad_ok = validar_edad(edad)
    celular_ok = validar_celular(celular)

    if nombre_ok and correo_ok and edad_ok and celular_ok:
        return True
    else:
        return False


# ============================================================
# 23. PROGRAMA DE PRUEBA
# ============================================================

if __name__ == "__main__":

    print("==========================================")
    print(" PRUEBAS DE VALIDACIONES BÁSICAS")
    print("==========================================")

    print()
    print("Correo:", validar_correo("estudiante@universidad.edu.co"))
    print("Correo:", validar_correo("correo-invalido"))

    print()
    print("Nombre:", validar_nombre("José Rodríguez"))
    print("Nombre:", validar_nombre("Juan123"))

    print()
    print("Longitud:", validar_longitud("Python", 3, 10))
    print("Longitud:", validar_longitud("Python", 10, 20))

    print()
    print("Rango:", validar_rango(75, 0, 100))
    print("Rango:", validar_rango(120, 0, 100))

    print()
    print("Celular:", validar_celular("3001234567"))
    print("Celular:", validar_celular("1234567890"))

    print()
    print("Escolaridad 0:", nivel_escolaridad(0))
    print("Escolaridad 4:", nivel_escolaridad(4))
    print("Escolaridad 9:", nivel_escolaridad(9))

    print()
    print("Estado:", estado_registro(1))
    print("Estado:", estado_registro(3))

    print()
    print("Tipo documento:", tipo_documento(1))
    print("Tipo usuario:", tipo_usuario(2))

    print()
    print("Procesamiento de varios correos:")
    ejemplo_procesamiento()
