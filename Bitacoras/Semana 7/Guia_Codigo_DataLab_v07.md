# Guía de Implementación: Código Python para DataLab v0.7

## 1. Datos generales

- **Proyecto integrador:** DataLab
- **Curso:** Lógica Computacional
- **Programa:** Ingeniería de Datos e Inteligencia Artificial
- **Semana:** 7 de 14
- **Modalidad:** Trabajo individual

## 2. Objetivo

Refactorizar DataLab para organizar su lógica mediante funciones con
responsabilidades claras.

Durante la implementación se trabajará con:

- Funciones.
- Parámetros.
- Argumentos.
- `return`.
- Alcance básico de variables.
- Reutilización de funciones.
- Modularización.
- Refactorización.
- Pruebas antes y después.
- Git y GitHub.

La meta es mantener el comportamiento de DataLab mientras se mejora su
estructura interna.

---

## 3. Recuperar el proyecto

Antes de comenzar:

```bash
git status
git pull
```

Verifica que estás trabajando sobre la versión de la Semana 6.

El punto de partida debe ser un DataLab funcional.

---

## 4. Ejecutar una línea base

Antes de modificar el código, ejecuta DataLab.

Registra resultados de:

- Clasificación.
- Procesamiento de registros.
- Resumen.
- Opciones válidas.
- Opciones inválidas.
- Salida del programa.

Esta información será la referencia para comprobar que la refactorización
no cambió el comportamiento.

---

## 5. Crear un punto de recuperación

Antes de refactorizar:

```bash
git status
git add .
git commit -m "chore: establece linea base antes de refactorizar"
```

Este commit crea una versión de recuperación.

Si la refactorización genera problemas, podrás revisar esta versión.

---

## 6. Identificar responsabilidades

Revisa `main.py` y localiza bloques que realizan tareas diferentes.

Busca responsabilidades como:

```text
Mostrar menú
Leer opción
Clasificar valor
Procesar registros
Generar resumen
Ejecutar operación
Controlar salida
```

No es necesario convertir cada línea en una función.

La pregunta es:

> ¿Este bloque realiza una tarea concreta que puede expresarse como una
> unidad independiente?

---

## 7. Crear una primera función

Ejemplo:

```python
def mostrar_mensaje():
    print("DataLab")
```

Para ejecutarla:

```python
mostrar_mensaje()
```

Recuerda:

```text
definir → crear la función
invocar → ejecutar la función
```

---

## 8. Crear una función con parámetro

Ejemplo:

```python
def saludar(nombre):
    print(f"Hola {nombre}")
```

Uso:

```python
saludar("Ana")
saludar("Carlos")
```

Aquí:

```text
nombre → parámetro
"Ana"  → argumento
```

El parámetro permite reutilizar la misma función con diferentes valores.

---

## 9. Crear una función con retorno

Ejemplo:

```python
def duplicar(valor):
    return valor * 2
```

Uso:

```python
resultado = duplicar(5)

print(resultado)
```

Resultado:

```text
10
```

La función calcula y retorna un valor.

---

## 10. Probar `return`

Realiza las siguientes pruebas:

```python
print(duplicar(5))
print(duplicar(0))
print(duplicar(10))
```

Resultados esperados:

```text
10
0
20
```

La función puede probarse sin ejecutar todo DataLab.

---

## 11. Diferenciar `print()` y `return`

Observa:

```python
def mostrar_clasificacion(clasificacion):
    print(clasificacion)
```

Esta función presenta información.

Ahora:

```python
def obtener_clasificacion(valor):
    clasificacion = clasificar_valor(valor)
    return clasificacion
```

Esta función entrega un resultado.

Uso:

```python
resultado = obtener_clasificacion(55)
print(resultado)
```

Cuando el resultado debe ser reutilizado por otro bloque, `return` es la
opción apropiada.

---

## 12. Revisar `clasificar_valor()`

DataLab ya tiene una función de clasificación.

Debe conservar una responsabilidad clara:

```python
def clasificar_valor(valor):
    # lógica existente
    return clasificacion
```

No se debe duplicar esta lógica en otros lugares.

Uso:

```python
clasificacion = clasificar_valor(valor)
```

La función recibe el valor y retorna la clasificación.

---

## 13. Refactorizar el menú

Extrae la presentación del menú:

```python
def mostrar_menu():
    print("1. Procesar registros")
    print("2. Mostrar información")
    print("3. Salir")
```

La función debe encargarse de mostrar las opciones.

No debe contener toda la lógica de procesamiento.

---

## 14. Leer la opción

Si DataLab necesita leer la opción del usuario, puede separarse esta tarea.

Ejemplo conceptual:

```python
def leer_opcion():
    opcion = input("Seleccione una opción: ")
    return opcion
```

Uso:

```python
opcion = leer_opcion()
```

La función obtiene la información y la retorna.

La validación debe mantenerse de acuerdo con la lógica existente del
proyecto.

---

## 15. Crear `procesar_registros()`

La lógica que procesa los registros puede separarse del menú.

Una estructura inicial puede ser:

```python
def procesar_registros(cantidad):
    # variables de estado
    contador_total = 0
    contador_altos = 0
    contador_normales = 0
    contador_bajos = 0

    suma_valores = 0
    existe_alto = False

    # procesamiento
    # ...

    return resultado
```

No copies automáticamente esta estructura.

Adapta la función al código que ya tienes en DataLab.

---

## 16. Reutilizar `clasificar_valor()`

Dentro del procesamiento:

```python
clasificacion = clasificar_valor(valor)
```

Después se pueden actualizar las variables de estado:

```python
if clasificacion == "ALTO":
    contador_altos += 1
elif clasificacion == "NORMAL":
    contador_normales += 1
elif clasificacion == "BAJO":
    contador_bajos += 1
```

La clasificación debe seguir centralizada en `clasificar_valor()`.

---

## 17. Mantener los acumuladores y banderas

La refactorización no elimina los conceptos de la Semana 6.

Se mantienen:

```python
contador_total = 0
contador_altos = 0
contador_normales = 0
contador_bajos = 0

suma_valores = 0
existe_alto = False
```

La diferencia es que ahora estas variables estarán organizadas dentro de
las funciones correspondientes y se utilizarán de forma controlada.

---

## 18. Retornar resultados del procesamiento

Cuando una función procesa información que será utilizada posteriormente,
debe retornar los resultados necesarios.

Una posibilidad sencilla es retornar varios valores:

```python
return (
    contador_total,
    contador_altos,
    contador_normales,
    contador_bajos,
    suma_valores,
    existe_alto
)
```

Luego:

```python
resultado = procesar_registros(cantidad)
```

Para esta semana no es necesario introducir estructuras de datos avanzadas
para resolver este problema.

---

## 19. Crear una función de resumen

La presentación del resumen puede separarse.

Ejemplo:

```python
def mostrar_resumen(
    total,
    altos,
    normales,
    bajos,
    suma,
    existe_alto
):
    print("Resumen")
    print(f"Total: {total}")
    print(f"ALTO: {altos}")
    print(f"NORMAL: {normales}")
    print(f"BAJO: {bajos}")
    print(f"Suma: {suma}")
    print(f"¿Existe ALTO?: {existe_alto}")
```

La función se concentra en mostrar la información.

---

## 20. Organizar `main()`

La función `main()` debe coordinar.

Una estructura conceptual:

```python
def main():
    mostrar_menu()

    opcion = leer_opcion()

    ejecutar_opcion(opcion)
```

Y al final:

```python
if __name__ == "__main__":
    main()
```

La estructura exacta puede variar.

Lo importante es reducir la lógica concentrada en `main()`.

---

## 21. Crear `ejecutar_opcion()`

Esta función puede decidir qué operación ejecutar.

Ejemplo conceptual:

```python
def ejecutar_opcion(opcion):
    if opcion == "1":
        procesar_registros(...)
    elif opcion == "2":
        mostrar_informacion()
    elif opcion == "3":
        controlar_salida()
```

Si el proyecto utiliza `match-case`, puede conservarse esa estructura:

```python
def ejecutar_opcion(opcion):
    match opcion:
        case "1":
            procesar_registros(...)
        case "2":
            mostrar_informacion()
        case "3":
            controlar_salida()
```

No es necesario reemplazar una estructura que ya funciona únicamente por
hacer la refactorización.

---

## 22. Evitar variables globales innecesarias

Evita un diseño como:

```python
contador_total = 0

def procesar():
    global contador_total
    contador_total += 1
```

Para esta etapa es preferible:

```python
def procesar(cantidad):
    contador_total = 0

    # procesamiento

    return contador_total
```

Y luego:

```python
total = procesar(cantidad)
```

La información entra mediante parámetros y sale mediante `return`.

---

## 23. Refactorización paso a paso

Utiliza este orden:

```text
1. Ejecutar DataLab
        ↓
2. Registrar resultados
        ↓
3. Crear commit de línea base
        ↓
4. Identificar responsabilidades
        ↓
5. Crear funciones pequeñas y claras
        ↓
6. Mover la lógica sin cambiarla
        ↓
7. Conectar funciones mediante parámetros y return
        ↓
8. Ejecutar las mismas pruebas
        ↓
9. Comparar resultados
        ↓
10. Crear commit de refactorización
```

---

## 24. Pruebas de regresión

Después de refactorizar, repetir las pruebas realizadas antes.

### Clasificación

Comprobar valores que produzcan:

```text
ALTO
NORMAL
BAJO
```

### Procesamiento

Comprobar diferentes cantidades de registros.

### Resumen

Comprobar que los contadores, acumulador y bandera mantienen sus resultados.

### Menú

Comprobar:

- Opciones válidas.
- Opciones inválidas.
- Salida.

### Objetivo

```text
Antes → comportamiento esperado
Después → mismo comportamiento esperado
```

---

## 25. Prueba de las funciones

Además de probar DataLab completo, prueba funciones individuales cuando
sea posible.

Ejemplo:

```python
print(duplicar(5))
```

Y:

```python
print(clasificar_valor(55))
```

La ventaja es que un error puede localizarse en una función específica.

---

## 26. Reto de implementación

Refactoriza DataLab para cumplir como mínimo:

```text
[ ] main() coordina
[ ] mostrar_menu() tiene responsabilidad clara
[ ] clasificar_valor() es reutilizable
[ ] procesar_registros() separa el procesamiento
[ ] existe una función para el resumen cuando sea conveniente
[ ] se utilizan parámetros
[ ] se utiliza return
[ ] se redujo la duplicación
[ ] no existen dependencias globales innecesarias
[ ] el comportamiento se mantiene
```

---

## 27. Documentación

Actualiza la documentación cuando la estructura del proyecto cambie.

Como mínimo, revisa:

- README.
- Pseudocódigo cuando corresponda.
- Diagrama de flujo cuando corresponda.
- Descripción de las funciones principales.

Ejemplo:

```text
mostrar_menu()
→ Presenta las opciones disponibles.

clasificar_valor(valor)
→ Recibe un valor y retorna ALTO, NORMAL o BAJO.

procesar_registros(cantidad)
→ Procesa los registros y retorna los resultados.

mostrar_resumen(...)
→ Presenta el resumen del procesamiento.
```

---

## 28. Git y GitHub

### Línea base

```bash
git status
git add .
git commit -m "chore: establece linea base antes de refactorizar"
```

### Refactorización

```bash
git add src/main.py
git commit -m "refactor: modulariza logica de DataLab"
```

### Documentación

Si corresponde:

```bash
git add docs/
git commit -m "docs: actualiza estructura modular"
```

### Publicar

```bash
git push
```

Comprueba que GitHub contiene la nueva versión.

---

## 29. Evidencias técnicas

El repositorio debe permitir verificar:

- Código modularizado.
- Funciones con responsabilidades claras.
- Uso de parámetros.
- Uso de `return`.
- Reutilización de `clasificar_valor()`.
- Pruebas antes y después.
- Documentación actualizada.
- Commit de línea base.
- Commit de refactorización.
- Repositorio GitHub actualizado.

---

## 30. Errores frecuentes de implementación

### Función demasiado grande

Si una función sigue realizando muchas tareas diferentes, analiza si alguna
responsabilidad puede separarse.

### Funciones sin propósito

No crees funciones solamente para aumentar el número de funciones.

### Uso innecesario de globales

Prefiere parámetros y `return`.

### `print()` en lugar de `return`

Si otro bloque necesita el resultado, debes retornarlo.

### Cambio accidental del comportamiento

No cambies la lógica funcional mientras refactorizas.

### Falta de pruebas

Ejecuta las pruebas antes y después.

---

## 31. Producto final

Al terminar debes tener:

```text
DataLab v0.7
│
├── main()
├── mostrar_menu()
├── leer_opcion()
├── ejecutar_opcion()
├── procesar_registros()
├── clasificar_valor()
└── mostrar_resumen()
```

La estructura exacta puede ser diferente si está justificada.

El objetivo es que DataLab conserve sus capacidades y tenga un código más
claro, reutilizable y mantenible.

---

## 32. Cierre técnico

La Semana 7 no agrega una gran funcionalidad.

Agrega una mejora fundamental en el diseño:

```text
Código concentrado
        ↓
Responsabilidades
        ↓
Funciones
        ↓
Parámetros
        ↓
Return
        ↓
Modularización
        ↓
Refactorización
```

Esta estructura prepara DataLab para trabajar con estructuras de datos en la
Semana 8.
