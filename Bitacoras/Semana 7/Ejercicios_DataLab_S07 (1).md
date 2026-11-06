# Taller de Ejercicios: Funciones, Modularización y Refactorización en DataLab

## 1. Datos generales

- **Proyecto integrador:** DataLab
- **Curso:** Lógica Computacional
- **Programa:** Ingeniería de Datos e Inteligencia Artificial
- **Semana:** 7 de 14
- **Modalidad:** Trabajo individual

## 2. Objetivo

Aplicar funciones, parámetros, argumentos, valores de retorno,
modularización y refactorización para mejorar la estructura interna de
DataLab sin cambiar su comportamiento esperado.

Los ejercicios avanzan desde funciones sencillas hasta la refactorización
del proyecto integrador.

---

# 3. Recomendaciones de trabajo

Antes de comenzar:

```bash
git status
git pull
```

Trabaja sobre la versión funcional de DataLab v0.6.

Antes de realizar cambios estructurales, crea una línea base:

```bash
git add .
git commit -m "chore: establece linea base antes de refactorizar"
```

---

# 4. Reto 1 — Primera función

### Contexto

Una función permite encapsular una tarea reutilizable.

### Objetivo

Crear una función que muestre un mensaje de bienvenida a DataLab.

### Requisitos

Crear:

```python
def mostrar_mensaje():
    ...
```

Debe mostrar:

```text
Bienvenido a DataLab
```

Después, invoca la función.

### Preguntas

1. ¿Qué parte del código corresponde a la definición?
2. ¿Qué parte corresponde a la invocación?
3. ¿Qué responsabilidad tiene la función?

---

# 5. Reto 2 — Parámetro y argumento

### Contexto

Las funciones pueden recibir información.

### Objetivo

Crear una función que reciba el nombre de un estudiante y muestre un
mensaje.

### Estructura esperada

```python
def saludar(nombre):
    ...
```

Prueba:

```python
saludar("Ana")
saludar("Carlos")
saludar("María")
```

### Preguntas

1. ¿Cuál es el parámetro?
2. ¿Cuál es el argumento?
3. ¿Qué ventaja tiene utilizar un parámetro?

---

# 6. Reto 3 — Función con retorno

### Contexto

Una función puede producir un resultado.

### Objetivo

Crear una función que reciba un número y retorne su doble.

```python
def duplicar(valor):
    ...
```

### Pruebas

```python
duplicar(5)
duplicar(0)
duplicar(10)
```

### Resultado esperado

```text
10
0
20
```

### Preguntas

1. ¿Qué recibe la función?
2. ¿Qué calcula?
3. ¿Qué retorna?
4. ¿Dónde queda almacenado el resultado?

---

# 7. Reto 4 — `print()` vs `return`

### Objetivo

Comparar dos funciones que realizan tareas diferentes.

Crear:

```python
def mostrar_resultado(valor):
    print(valor)
```

y:

```python
def obtener_resultado(valor):
    return valor
```

### Actividad

Utiliza ambas funciones y explica:

> ¿Cuál permite que otro bloque del programa utilice el resultado?

### Evidencia

Incluye el código y una explicación breve.

---

# 8. Reto 5 — Función de clasificación

### Contexto

DataLab ya utiliza clasificación de valores.

### Objetivo

Crear o revisar una función:

```python
def clasificar_valor(valor):
    ...
    return clasificacion
```

Debe conservar las reglas utilizadas actualmente en DataLab.

### Pruebas

Prueba valores que produzcan:

```text
ALTO
NORMAL
BAJO
```

### Requisito

No duplicar la lógica de clasificación fuera de la función.

### Pregunta

¿Por qué es mejor reutilizar `clasificar_valor()`?

---

# 9. Reto 6 — Contador mediante una función

### Contexto

Una función puede procesar varios valores.

### Datos

```python
valores = [22, 55, 72, 38, 61]
```

### Objetivo

Crear una función que reciba una lista y retorne la cantidad de valores
procesados.

```python
def contar_registros(valores):
    ...
```

### Resultado esperado

```text
5
```

### Restricción

Utilizar un contador.

### Pregunta

¿Por qué el contador debe inicializarse dentro de la función?

---

# 10. Reto 7 — Acumulador mediante una función

### Datos

```python
valores = [10, 20, 30, 40]
```

### Objetivo

Crear:

```python
def calcular_suma(valores):
    ...
```

Debe retornar:

```text
100
```

### Requisitos

- Utilizar un acumulador.
- Recorrer los valores.
- Retornar el resultado.
- No utilizar una variable global para almacenar la suma.

---

# 11. Reto 8 — Función con clasificación y resumen

### Datos

```python
valores = [20, 55, 80, 40, 70]
```

### Objetivo

Crear una función que procese los valores y cuente cuántos son:

```text
ALTO
NORMAL
BAJO
```

Debe utilizar:

```python
clasificar_valor(valor)
```

### Resultado esperado

El programa debe generar los contadores correspondientes a las categorías
según las reglas actuales de DataLab.

### Requisitos

- Función con parámetro.
- Contadores.
- Reutilización de `clasificar_valor()`.
- `return` de resultados.

---

# 12. Reto 9 — Separar el menú

### Contexto

Parte de la lógica de DataLab está concentrada en `main()`.

### Objetivo

Extraer la presentación del menú a:

```python
def mostrar_menu():
    ...
```

### Requisitos

`mostrar_menu()` debe:

- Mostrar las opciones.
- No procesar registros.
- No calcular el resumen.
- No controlar toda la lógica del programa.

### Pregunta

¿Qué responsabilidad queda ahora en `main()`?

---

# 13. Reto 10 — Leer una opción

### Objetivo

Crear una función para obtener la opción seleccionada:

```python
def leer_opcion():
    ...
    return opcion
```

### Uso esperado

```python
opcion = leer_opcion()
```

### Preguntas

1. ¿Qué información recibe la función?
2. ¿Qué información produce?
3. ¿Por qué utilizar `return`?

---

# 14. Reto 11 — Separar `ejecutar_opcion()`

### Objetivo

Crear una función que reciba la opción seleccionada y determine qué
operación debe ejecutarse.

Una estructura posible:

```python
def ejecutar_opcion(opcion):
    ...
```

Puede utilizar `if` o `match-case`, de acuerdo con la estructura actual de
DataLab.

### Requisito

La función debe coordinar la opción, no contener toda la lógica de cada
operación.

---

# 15. Reto 12 — Crear `procesar_registros()`

### Contexto

La lógica que procesa registros no debería estar mezclada con la lógica
del menú.

### Objetivo

Separar el procesamiento en:

```python
def procesar_registros(cantidad):
    ...
```

### Debe considerar

- Cantidad de registros.
- Clasificación.
- Contadores.
- Acumulador.
- Bandera.
- Resultado del procesamiento.

### Pregunta

¿Qué información necesita recibir la función y qué información debería
retornar?

---

# 16. Reto 13 — Función de resumen

### Objetivo

Separar la presentación del resumen.

Crear una función que reciba los resultados y los muestre.

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
    ...
```

### Requisito

La función debe concentrarse en mostrar la información.

### Pregunta

¿Por qué es conveniente separar el cálculo del resumen de su presentación?

---

# 17. Reto 14 — Reducir la lógica de `main()`

### Antes

Analiza tu `main()` actual.

Identifica:

- Menú.
- Entrada.
- Procesamiento.
- Clasificación.
- Resumen.
- Salida.

### Después

Busca llegar a una estructura semejante a:

```text
main()
 ├── mostrar_menu()
 ├── leer_opcion()
 ├── ejecutar_opcion()
 │     └── procesar_registros()
 │            └── clasificar_valor()
 └── mostrar_resumen()
```

### Pregunta

¿Qué responsabilidades quedaron fuera de `main()`?

---

# 18. Reto 15 — Detectar variables globales

### Actividad

Revisa el proyecto y busca variables definidas fuera de las funciones que
se utilizan para transportar información.

Para cada variable responde:

| Variable | ¿Es global? | ¿Puede ser parámetro? | ¿Puede retornarse? |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### Objetivo

Identificar dependencias globales innecesarias.

---

# 19. Reto 16 — Refactorizar sin cambiar el comportamiento

### Objetivo

Realizar una refactorización completa de una parte de DataLab.

### Procedimiento

```text
1. Ejecutar DataLab.
2. Registrar resultados.
3. Crear commit de línea base.
4. Identificar una responsabilidad.
5. Crear una función.
6. Pasar información mediante parámetros.
7. Retornar resultados cuando sea necesario.
8. Ejecutar nuevamente las pruebas.
9. Comparar resultados.
```

### Condición

El comportamiento esperado debe mantenerse.

---

# 20. Reto 17 — Pruebas antes y después

Registra los resultados de DataLab antes de refactorizar.

| Prueba | Antes | Después | ¿Coincide? |
|---|---|---|---|
| Clasificación | | | |
| Procesamiento | | | |
| Resumen | | | |
| Opción válida | | | |
| Opción inválida | | | |
| Salida | | | |

### Objetivo

Comprobar que la refactorización no cambió el comportamiento.

---

# 21. Reto 18 — Pruebas de funciones

Selecciona al menos tres funciones de DataLab.

Para cada una define casos de prueba.

| Función | Entrada | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### Ejemplos

```text
clasificar_valor(55)
duplicar(5)
contar_registros([10, 20, 30])
```

---

# 22. Reto 19 — Análisis de responsabilidad

Para cada función principal de tu proyecto completa:

| Función | ¿Qué recibe? | ¿Qué hace? | ¿Qué retorna? |
|---|---|---|---|
| `mostrar_menu()` | | | |
| `leer_opcion()` | | | |
| `clasificar_valor()` | | | |
| `procesar_registros()` | | | |
| `mostrar_resumen()` | | | |
| `main()` | | | |

### Pregunta

¿Existe alguna función que esté realizando demasiadas responsabilidades?

---

# 23. Reto 20 — Documentar las funciones

Documenta las funciones principales con una descripción breve.

Ejemplo:

```text
clasificar_valor(valor)
Responsabilidad:
Recibir un valor y retornar su clasificación.

procesar_registros(cantidad)
Responsabilidad:
Procesar una cantidad de registros y retornar los resultados.

mostrar_resumen(...)
Responsabilidad:
Presentar el resumen generado por el procesamiento.
```

### Objetivo

Que otro estudiante pueda comprender la función sin leer todo el programa.

---

# 24. Reto final — DataLab v0.7

## Objetivo

Refactorizar DataLab para convertirlo en una versión modular mediante
funciones.

### Requisitos mínimos

```text
[ ] main() actúa principalmente como coordinador.
[ ] Existen funciones con responsabilidades claras.
[ ] Se utilizan parámetros.
[ ] Se utilizan argumentos.
[ ] Se utiliza return.
[ ] Se reutiliza clasificar_valor().
[ ] Se separa el procesamiento del menú.
[ ] Se reduce la duplicación.
[ ] Se evitan variables globales innecesarias.
[ ] Se mantienen las capacidades anteriores.
[ ] Se realizan pruebas antes y después.
[ ] Se actualiza la documentación.
[ ] Se crea commit de línea base.
[ ] Se crea commit de refactorización.
[ ] Se realiza push a GitHub.
```

---

# 25. Estructura esperada

La estructura puede variar, pero debe existir una separación clara de
responsabilidades.

Una posibilidad:

```text
DataLab
│
├── main()
│
├── mostrar_menu()
│
├── leer_opcion()
│
├── ejecutar_opcion()
│
├── procesar_registros()
│
├── clasificar_valor()
│
└── mostrar_resumen()
```

No se evalúa que todos tengan exactamente estos nombres.

Se evalúa que la organización tenga sentido y pueda ser explicada.

---

# 26. Preguntas de reflexión

Responde con tus propias palabras:

1. ¿Qué problema resuelven las funciones?
2. ¿Cuál es la diferencia entre un parámetro y un argumento?
3. ¿Por qué `return` es importante?
4. ¿Cuándo conviene utilizar una función?
5. ¿Qué diferencia existe entre `print()` y `return`?
6. ¿Qué ventaja tiene dividir DataLab en funciones?
7. ¿Por qué no es conveniente depender innecesariamente de variables
   globales?
8. ¿Qué significa refactorizar?
9. ¿Qué riesgo existe al refactorizar un programa que ya funciona?
10. ¿Por qué fue útil crear un commit antes de comenzar la refactorización?

---

# 27. Entregables

El repositorio debe contener:

### Código

- Código DataLab v0.7 modularizado.
- Funciones con responsabilidades claras.
- Uso de parámetros.
- Uso de valores de retorno.
- Reutilización de funciones.

### Documentación

- Documentación actualizada.
- Pseudocódigo actualizado cuando corresponda.
- Diagrama actualizado cuando corresponda.

### Evidencias

- Pruebas antes de refactorizar.
- Pruebas después de refactorizar.
- Commit de línea base.
- Commit de refactorización.
- Repositorio GitHub actualizado.

---

# 28. Checklist final

Antes de entregar:

```text
[ ] Puedo explicar qué es una función.
[ ] Puedo diferenciar parámetro y argumento.
[ ] Puedo explicar return.
[ ] Puedo diferenciar print() y return.
[ ] Puedo identificar responsabilidades.
[ ] main() ya no contiene toda la lógica.
[ ] Mi código tiene menos duplicación.
[ ] Evité dependencias globales innecesarias.
[ ] Probé DataLab antes de refactorizar.
[ ] Probé DataLab después de refactorizar.
[ ] Los resultados esperados se mantienen.
[ ] Actualicé la documentación.
[ ] Creé el commit de línea base.
[ ] Creé el commit de refactorización.
[ ] Hice push al repositorio.
[ ] Puedo explicar por qué dividí el código de esa manera.
```

---

# 29. Producto de cierre

Al finalizar la actividad tendrás:

**DataLab v0.7 — Código modularizado mediante funciones.**

El proyecto conserva las funcionalidades anteriores, pero ahora presenta una
estructura interna más clara, reutilizable y mantenible.

La siguiente semana utilizarás esta modularización como base para trabajar
con **estructuras de datos**.
