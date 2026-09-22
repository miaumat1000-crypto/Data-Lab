# Programa de Ingeniería de Datos e Inteligencia Artificial

**Espacio Académico:** Lógica Computacional  
**Actividad:** Semana 04 - Ciclos `for` y `range`

---

# Guía del estudiante — Semana 04

## 1. Introducción

En las semanas anteriores se trabajó con estructuras de decisión y validación de datos. En la Semana 3 se construyeron validaciones para diferentes tipos de información, por ejemplo:

- Correos electrónicos válidos.
- Nombres válidos.
- Números dentro de rangos permitidos.
- Valores pertenecientes a opciones determinadas.
- Datos vacíos o incompletos.

En esta semana se dará un paso adicional: **procesar múltiples datos utilizando ciclos**.

El objetivo no es solamente aprender `for` y `range()`. También se busca que el código construido durante las semanas anteriores pueda **reutilizarse sin copiar y pegar las mismas validaciones**.

La progresión será:

> **Validaciones → funciones → módulos → ciclos → procesamiento de múltiples registros → resultados e indicadores → arquitectura reutilizable**

La actividad continúa el desarrollo de **DataLab**, por lo que los ejercicios deben entenderse como pequeñas evoluciones de un sistema que posteriormente podrá procesar datos reales.

---

# 2. ¿Qué aprenderemos?

Al finalizar la actividad podrás:

1. Comprender qué es un ciclo.
2. Utilizar `for` para repetir instrucciones.
3. Utilizar `range()` para controlar la cantidad de iteraciones.
4. Procesar varios datos con una misma lógica.
5. Reutilizar funciones desarrolladas anteriormente.
6. Organizar validaciones en un módulo.
7. Utilizar contadores y acumuladores.
8. Identificar datos válidos e inválidos.
9. Calcular indicadores sencillos de calidad.
10. Integrar ciclos y validaciones dentro de DataLab.
11. Actualizar el pseudocódigo y el diagrama de flujo.
12. Registrar los avances mediante Git y GitHub.

---

# 3. Punto de partida: reutilizar lo construido en Semana 3

En Semana 3 se trabajó con validaciones y selección. La idea ahora es **reutilizar esas reglas**.

Por ejemplo:

```python
def validar_nombre(nombre):
    nombre = nombre.strip()

    if not nombre:
        return False

    return nombre.replace(" ", "").isalpha()
```

Una validación sencilla de correo:

```python
def validar_correo(correo):
    correo = correo.strip()

    if not correo:
        return False

    return "@" in correo and "." in correo
```

Y una validación de rango:

```python
def validar_rango(valor, minimo, maximo):
    return minimo <= valor <= maximo
```

Estas funciones pueden utilizarse muchas veces.

```python
print(validar_nombre("Ana Pérez"))
print(validar_nombre("12345"))

print(validar_correo("ana@gmail.com"))
print(validar_correo("correo-invalido"))

print(validar_rango(75, 0, 100))
```

Es preferible que una función de validación **retorne `True` o `False` y no realice directamente un `print()`**, porque así puede reutilizarse en diferentes partes del programa.

---

# 4. ¿Por qué utilizar módulos?

A medida que DataLab crece, colocar todas las funciones dentro de `main.py` puede hacer que el programa sea difícil de mantener.

Una primera organización puede ser:

```text
DataLab/
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   ├── main.py
│   └── validaciones.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
├── tests/
├── docs/
└── notebooks/
```

El archivo `validaciones.py` puede contener las reglas relacionadas con la validación.

## 4.1. Archivo `validaciones.py`

```python
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
```

## 4.2. Utilizar las funciones desde `main.py`

```python
from validaciones import validar_nombre, validar_correo, validar_rango

nombre = input("Ingrese su nombre: ")
correo = input("Ingrese su correo: ")
edad = int(input("Ingrese su edad: "))

print(validar_nombre(nombre))
print(validar_correo(correo))
print(validar_rango(edad, 0, 120))
```

También puedes importar el módulo completo:

```python
import validaciones

nombre = input("Ingrese su nombre: ")

if validaciones.validar_nombre(nombre):
    print("Nombre válido")
else:
    print("Nombre inválido")
```

---

# 5. ¿Necesitamos una librería externa?

Para esta semana **no es necesario utilizar una librería externa para implementar las validaciones básicas**.

Python ya proporciona herramientas suficientes para trabajar con cadenas de texto, números, rangos, conversión de tipos, comparaciones, ciclos y funciones.

Por ejemplo:

```python
texto.strip()
texto.lower()
texto.isalpha()
texto.isdigit()
```

La intención es comprender primero la lógica de las validaciones y su reutilización.

> **Principio:** primero diseñamos una solución reutilizable; posteriormente evaluamos si una librería puede mejorarla.

---

# 6. Concepto de ciclo

Un ciclo permite repetir un conjunto de instrucciones.

Sin ciclo:

```python
print("Procesando...")
print("Procesando...")
print("Procesando...")
print("Procesando...")
print("Procesando...")
```

Con un ciclo:

```python
for i in range(5):
    print("Procesando...")
```

La instrucción se ejecuta cinco veces.

---

# 7. El ciclo `for`

La estructura básica es:

```python
for variable in secuencia:
    instrucciones
```

Ejemplo:

```python
for i in range(5):
    print(i)
```

Resultado:

```text
0
1
2
3
4
```

Observa que `range(5)` genera cinco valores comenzando en `0`.

---

# 8. La función `range()`

`range()` permite definir una secuencia de números.

### Un parámetro

```python
range(5)
```

Genera:

```text
0 1 2 3 4
```

### Dos parámetros

```python
range(2, 7)
```

Genera:

```text
2 3 4 5 6
```

El segundo valor es el límite superior y **no se incluye**.

### Tres parámetros

```python
range(2, 10, 2)
```

Genera:

```text
2 4 6 8
```

La estructura es:

```python
range(inicio, fin, paso)
```

---

# 9. Ejemplo: procesar una cantidad de registros

```python
cantidad = 5

for i in range(cantidad):
    print("Procesando estudiante", i + 1)
```

Resultado:

```text
Procesando estudiante 1
Procesando estudiante 2
Procesando estudiante 3
Procesando estudiante 4
Procesando estudiante 5
```

El `+ 1` se utiliza para mostrar al usuario una numeración que empiece en 1.

---

# 10. Ejercicio 1 — Validar múltiples nombres

## Objetivo

Utilizar una función de validación desarrollada anteriormente dentro de un ciclo `for`.

```python
from validaciones import validar_nombre

for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")

    if validar_nombre(nombre):
        print("Nombre válido")
    else:
        print("Nombre inválido")
```

Prueba nombres como:

```text
Ana Pérez
Carlos Gómez
12345
María López
Juan_123
```

Analiza:

1. ¿Cuántas veces se ejecuta `validar_nombre()`?
2. ¿Cuántas veces se ejecuta el `if`?
3. ¿Qué parte cambia en cada iteración?
4. ¿Qué parte permanece igual?

---

# 11. Ejercicio 2 — Validar múltiples correos

```python
from validaciones import validar_correo

for i in range(5):
    correo = input(f"Ingrese el correo {i + 1}: ")

    if validar_correo(correo):
        print("Correo válido")
    else:
        print("Correo inválido")
```

Prueba:

```text
ana@gmail.com
correo
usuario@dominio.com
@test.com
usuario@
```

---

# 12. Ejercicio 3 — Validar números dentro de un rango

Supongamos que un valor debe estar entre `0` y `100`.

```python
from validaciones import validar_rango

for i in range(5):
    valor = float(input(f"Ingrese el valor {i + 1}: "))

    if validar_rango(valor, 0, 100):
        print("Valor válido")
    else:
        print("Valor fuera del rango")
```

Prueba especialmente:

```text
0
1
50
99
100
101
-1
```

---

# 13. Ejercicio 4 — Validar opciones

Supongamos que un sistema permite seleccionar:

```text
1 - Estudiante
2 - Docente
3 - Administrativo
```

Función:

```python
def validar_opcion(opcion):
    return opcion in [1, 2, 3]
```

Uso:

```python
for i in range(5):
    opcion = int(input("Seleccione una opción (1, 2 o 3): "))

    if validar_opcion(opcion):
        print("Opción válida")
    else:
        print("Opción inválida")
```

---

# 14. Ejercicio 5 — Contar datos válidos e inválidos

Queremos procesar diez correos y determinar cuántos son válidos e inválidos.

```python
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
```

La instrucción:

```python
validos += 1
```

equivale a:

```python
validos = validos + 1
```

Cada vez que encontramos un dato válido, el contador aumenta.

---

# 15. Ejercicio 6 — Clasificar valores

Categorías:

- `BAJO`: 0 a 59.
- `NORMAL`: 60 a 79.
- `ALTO`: 80 a 100.

Función:

```python
def clasificar_valor(valor):
    if valor < 60:
        return "BAJO"
    elif valor < 80:
        return "NORMAL"
    else:
        return "ALTO"
```

Procesamiento:

```python
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
```

---

# 16. Ejercicio 7 — Resumen de nombres

Procesa ocho nombres utilizando `validar_nombre()`.

El programa debe indicar:

- Cantidad de nombres válidos.
- Cantidad de nombres inválidos.
- Porcentaje de nombres válidos.

```python
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
```

---

# 17. Ejercicio 8 — Validar edades

Una edad válida debe estar entre `0` y `120`.

```python
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
```

Prueba:

```text
-1
0
1
18
50
119
120
121
```

---

# 18. Ejercicio 9 — Validar un registro de usuario

Un registro contiene:

- Nombre.
- Correo.
- Edad.

El registro será válido solamente si **todos sus campos son válidos**.

```python
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
```

---

# 19. Ejercicio 10 — Calidad de datos

Cada registro contiene:

```text
Nombre
Correo
Edad
Valor
```

Reglas:

| Campo | Regla |
|---|---|
| Nombre | Debe ser válido |
| Correo | Debe tener una estructura básica válida |
| Edad | 0 a 120 |
| Valor | 0 a 100 |

El registro será válido solamente si todos los campos cumplen su regla.

```python
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
```

---

# 20. Ejercicio 11 — Indicador de calidad

Un indicador sencillo puede calcularse así:

```text
Calidad = registros válidos / registros totales × 100
```

En Python:

```python
calidad = (validos / total) * 100
```

Por ejemplo:

```python
print("Calidad de los datos:", calidad, "%")
```

Si procesamos 20 registros y 17 son válidos:

```text
Calidad = 17 / 20 × 100
```

Determina el resultado antes de ejecutarlo en Python.

---

# 21. Ejercicio 12 — Reto integrador DataLab

Este es el ejercicio principal de la semana.

El objetivo es integrar:

- Funciones.
- Módulos.
- Validaciones.
- `for`.
- `range()`.
- Contadores.
- Indicadores.
- Pruebas.
- Git.
- GitHub.

## Situación

DataLab debe procesar una cantidad definida de registros.

Cada registro contiene:

```text
Nombre
Correo
Edad
Valor
```

El usuario debe indicar cuántos registros desea procesar:

```text
¿Cuántos registros desea procesar? 10
```

El programa debe procesar los diez registros mediante un ciclo.

---

# 22. Diseño del algoritmo

## Entrada

```text
Cantidad de registros
Nombre
Correo
Edad
Valor
```

## Proceso

Para cada registro:

1. Leer los datos.
2. Validar nombre.
3. Validar correo.
4. Validar edad.
5. Validar valor.
6. Determinar si el registro es válido.
7. Actualizar contadores.

Al finalizar:

1. Mostrar total.
2. Mostrar válidos.
3. Mostrar inválidos.
4. Calcular porcentaje de calidad.

## Salida

```text
Total de registros
Registros válidos
Registros inválidos
Porcentaje de calidad
```

---

# 23. Pseudocódigo del reto

```text
INICIO

    LEER cantidad

    validos = 0
    invalidos = 0

    PARA cada registro desde 1 hasta cantidad

        LEER nombre
        LEER correo
        LEER edad
        LEER valor

        nombre_valido = validar_nombre(nombre)
        correo_valido = validar_correo(correo)
        edad_valida = validar_rango(edad, 0, 120)
        valor_valido = validar_rango(valor, 0, 100)

        SI todos los campos son válidos ENTONCES
            validos = validos + 1
        SI NO
            invalidos = invalidos + 1
        FIN SI

    FIN PARA

    calidad = validos / cantidad * 100

    MOSTRAR total
    MOSTRAR validos
    MOSTRAR invalidos
    MOSTRAR calidad

FIN
```

Debes analizar este pseudocódigo y adaptarlo a tu implementación.

---

# 24. Implementación inicial del reto

```python
from validaciones import validar_nombre, validar_correo, validar_rango


cantidad = int(input("¿Cuántos registros desea procesar? "))

validos = 0
invalidos = 0

for i in range(cantidad):

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


calidad = (validos / cantidad) * 100

print("\n===== RESUMEN =====")
print("Total:", cantidad)
print("Válidos:", validos)
print("Inválidos:", invalidos)
print("Calidad:", calidad, "%")
```

---

# 25. ¿Dónde está la reutilización?

La arquitectura puede entenderse así:

```text
main.py
   │
   ├── validar_nombre()
   ├── validar_correo()
   └── validar_rango()
             │
             ▼
       validaciones.py
```

El ciclo no necesita conocer cómo funciona internamente cada validación.

Por ejemplo:

```python
validar_correo(correo)
```

solamente necesita recibir un correo y devolver un resultado.

Esto permite cambiar la implementación de la validación posteriormente sin modificar toda la lógica del procesamiento.

---

# 26. Una regla importante de arquitectura

Evita copiar las mismas reglas dentro del ciclo.

En lugar de repetir:

```python
for i in range(10):

    if "@" in correo:
        ...

    if "." in correo:
        ...
```

si esa lógica ya existe en una función, reutilízala:

```python
for i in range(10):

    if validar_correo(correo):
        ...
```

La idea fundamental es:

> **Una responsabilidad debe tener un lugar claro dentro del programa.**

Las validaciones pertenecen al módulo de validaciones.

El procesamiento de múltiples registros pertenece a la lógica principal.

---

# 27. ¿Por qué no crear un módulo `ciclos.py`?

No es necesario crear un archivo llamado:

```text
ciclos.py
```

El `for` es una estructura de control de Python, no una responsabilidad independiente del sistema.

En cambio, sí tiene sentido separar:

```text
validaciones.py
```

porque contiene un conjunto de funciones relacionadas con una responsabilidad concreta.

A medida que DataLab crezca podremos identificar nuevas responsabilidades y crear nuevos módulos cuando realmente sea necesario.

---

# 28. Pruebas

El programa debe probarse con diferentes cantidades de registros.

Como mínimo:

### Prueba 1

```text
Cantidad = 1
```

### Prueba 2

```text
Cantidad = 3
```

### Prueba 3

```text
Cantidad = 5
```

### Prueba 4

```text
Cantidad = 10
```

También debes probar:

- Todos los registros válidos.
- Todos los registros inválidos.
- Mezcla de válidos e inválidos.
- Valores en los límites.
- Valores por fuera de los límites.
- Correos válidos e inválidos.
- Nombres válidos e inválidos.

---

# 29. Pruebas de límites

Para:

```python
validar_rango(edad, 0, 120)
```

prueba:

```text
-1
0
1
119
120
121
```

Para:

```python
validar_rango(valor, 0, 100)
```

prueba:

```text
-1
0
1
99
100
101
```

Estas pruebas permiten identificar errores en condiciones como:

```python
valor < 100
```

cuando realmente se necesitaba:

```python
valor <= 100
```

---

# 30. Git y GitHub

Antes de comenzar verifica que tienes la última versión del proyecto:

```bash
git status
```

Después:

```bash
git pull
```

Realiza los cambios correspondientes a la Semana 4.

Puedes hacer un commit como:

```bash
git add src/
git commit -m "feat: agrega procesamiento repetitivo"
git push
```

Si modificaste documentación:

```bash
git add README.md docs/
git commit -m "docs: actualiza documentacion semana 4"
git push
```

Los mensajes de commit deben describir qué cambió.

---

# 31. Entregable

Al finalizar la actividad debes tener en tu repositorio:

```text
DataLab/
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   ├── main.py
│   └── validaciones.py
├── data/
├── tests/
├── docs/
└── notebooks/
```

La estructura puede adaptarse al estado actual de tu proyecto.

Debes entregar como mínimo:

- Código funcional.
- Uso de `for`.
- Uso de `range()`.
- Funciones reutilizables.
- Módulo de validaciones.
- Procesamiento de múltiples registros.
- Contadores.
- Indicador de calidad.
- Pruebas realizadas.
- Pseudocódigo actualizado.
- Diagrama de flujo actualizado.
- README actualizado.
- Commits realizados en Git.
- Código publicado en GitHub.

---

# 32. Criterios de finalización

- [ ] Comprendo qué hace un ciclo `for`.
- [ ] Comprendo cómo funciona `range()`.
- [ ] Puedo procesar una cantidad determinada de registros.
- [ ] Reutilizo las validaciones de la Semana 3.
- [ ] Las validaciones están organizadas en un módulo.
- [ ] Evité copiar y pegar las mismas reglas.
- [ ] Utilizo funciones que retornan resultados.
- [ ] Utilizo contadores.
- [ ] Calculo un indicador de calidad.
- [ ] Probé diferentes cantidades de registros.
- [ ] Probé valores válidos e inválidos.
- [ ] Probé valores límite.
- [ ] Actualicé el pseudocódigo.
- [ ] Actualicé el diagrama de flujo.
- [ ] Actualicé el README.
- [ ] Realicé commits descriptivos.
- [ ] Hice `push` al repositorio.

---

# 33. Reflexión — Técnica Feynman

Explica con tus propias palabras:

1. ¿Qué problema resuelve un ciclo?
2. ¿Por qué `range(5)` produce cinco iteraciones?
3. ¿Qué diferencia existe entre una función y un ciclo?
4. ¿Por qué una validación debería ser una función reutilizable?
5. ¿Por qué separar las validaciones en un módulo?
6. ¿Qué función cumplen los contadores?
7. ¿Qué diferencia existe entre procesar un registro y procesar muchos registros?
8. ¿Qué ocurre si cambia una regla de validación?
9. ¿Por qué no conviene copiar y pegar una validación?
10. ¿Cómo contribuye esta arquitectura al crecimiento de DataLab?

---

# 34. Evolución de DataLab

Al finalizar esta semana, DataLab pasa conceptualmente de:

```text
DataLab
   │
   └── Procesa un registro
```

a:

```text
DataLab
   │
   ├── recibe N registros
   │
   ├── valida cada registro
   │
   ├── procesa cada registro
   │
   ├── cuenta resultados
   │
   └── genera indicadores
```

La evolución es importante porque los sistemas de datos reales normalmente no procesan un único dato.

Procesan:

```text
1 registro
      ↓
N registros
      ↓
muchos registros
      ↓
conjuntos de datos
      ↓
procesos automatizados
```

En las siguientes etapas de DataLab esta lógica podrá evolucionar hacia el procesamiento de datos provenientes de fuentes estructuradas y posteriormente hacia procesos de datos más cercanos a escenarios reales.

---

# 35. Reto adicional — Diseña tu propia validación

Como actividad opcional, crea una nueva validación que no haya sido implementada anteriormente.

Algunas posibilidades:

- Código postal.
- Teléfono.
- Documento de identidad.
- Código de producto.
- Edad mínima para una actividad.
- Nota académica.
- Código de estudiante.
- Valor monetario.
- Estado permitido de un registro.

La función debe seguir el mismo principio:

```python
def validar_dato(dato):
    # reglas
    return True
```

o:

```python
def validar_dato(dato):
    # reglas
    return False
```

Después intégrala a un ciclo `for` y procesa múltiples valores.

---

# 36. Idea central de la Semana 4

La meta de esta semana no es simplemente escribir:

```python
for i in range(10):
```

La meta es comprender que un programa puede:

1. Definir una regla una sola vez.
2. Convertir esa regla en una función.
3. Organizar funciones relacionadas en módulos.
4. Reutilizar esas funciones.
5. Procesar múltiples datos mediante ciclos.
6. Acumular resultados.
7. Generar información útil a partir de esos resultados.

En otras palabras:

> **No se trata solamente de repetir instrucciones. Se trata de diseñar una solución que pueda repetirse sin repetir el código.**

---

## Fin de la guía

**Semana 04 — Ciclos `for` y `range()`**  
**Programa de Ingeniería de Datos e Inteligencia Artificial**  
**Espacio Académico: Lógica Computacional**
