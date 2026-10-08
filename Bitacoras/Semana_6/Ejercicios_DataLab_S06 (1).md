# Taller de Ejercicios: Contadores, Acumuladores y Banderas en DataLab

## 1. Datos generales

-   **Proyecto integrador:** DataLab
-   **Curso:** Lógica Computacional
-   **Semana:** 6 de 14
-   **Modalidad:** Trabajo individual

## 2. Objetivo

Aplicar los conceptos de la Semana 6 para que DataLab procese múltiples
registros, conserve información durante el ciclo y genere resultados
agregados.

Los ejercicios deben implementarse en Python y, cuando corresponda,
integrarse al proyecto DataLab.

------------------------------------------------------------------------

# 3. Reto 1 --- Contador de registros

### Contexto

DataLab procesa una cantidad definida de valores.

### Objetivo

Recorrer una lista y contar cuántos registros fueron procesados.

### Datos

``` python
valores = [22.5, 55.1, 72.3, 38.7, 61.4]
```

### Resultado esperado

``` text
Registros procesados: 5
```

### Requisitos

-   Utilizar un contador.
-   Inicializarlo antes del ciclo.
-   Incrementarlo una vez por cada registro.
-   Mostrar el resultado al finalizar.

------------------------------------------------------------------------

# 4. Reto 2 --- Contador por categoría

### Contexto

DataLab clasifica cada valor como:

``` text
ALTO
NORMAL
BAJO
```

### Objetivo

Crear un contador para cada categoría.

### Requisitos

Utilizar:

``` python
contador_altos = 0
contador_normales = 0
contador_bajos = 0
```

Actualizar el contador correspondiente después de clasificar cada valor.

### Resultado

Mostrar:

``` text
ALTO:
NORMAL:
BAJO:
```

Debe cumplirse:

``` text
ALTO + NORMAL + BAJO = TOTAL
```

------------------------------------------------------------------------

# 5. Reto 3 --- Acumulador de valores

### Contexto

DataLab necesita conocer la suma de todos los valores procesados.

### Objetivo

Crear un acumulador.

### Datos

``` python
valores = [10, 20, 30, 40, 50]
```

### Resultado esperado

``` text
Suma de valores: 150
```

### Requisitos

-   Inicializar `suma_valores` en `0`.
-   Sumar cada valor dentro del ciclo.
-   Mostrar el resultado al finalizar.
-   No calcular la suma manualmente dentro del programa.

------------------------------------------------------------------------

# 6. Reto 4 --- Bandera de existencia

### Contexto

DataLab necesita saber si durante el procesamiento apareció al menos un
valor `ALTO`.

### Objetivo

Utilizar una bandera.

### Inicio

``` python
existe_alto = False
```

Cuando aparezca un `ALTO`:

``` python
existe_alto = True
```

### Resultado

Mostrar:

``` text
¿Existe algún ALTO?: True
```

o:

``` text
¿Existe algún ALTO?: False
```

según los datos procesados.

------------------------------------------------------------------------

# 7. Reto 5 --- Procesamiento y resumen

### Objetivo

Combinar contador, acumulador y bandera.

### Datos

``` python
valores = [22.5, 55.1, 72.3, 38.7, 61.4]
```

### El programa debe generar

``` text
===== RESUMEN =====
Total de registros:
ALTO:
NORMAL:
BAJO:
Suma de valores:
¿Existe algún ALTO?:
```

### Debe utilizar

-   Contador total.
-   Contador ALTO.
-   Contador NORMAL.
-   Contador BAJO.
-   Acumulador.
-   Bandera.

------------------------------------------------------------------------

# 8. Reto 6 --- Conjunto sin valores ALTO

Utiliza un conjunto de datos donde todos los valores resulten `NORMAL`.

Comprueba:

``` text
ALTO = 0
BAJO = 0
existe_alto = False
```

Explica por qué la bandera no cambia.

------------------------------------------------------------------------

# 9. Reto 7 --- Un solo ALTO

Construye un conjunto de datos donde exista exactamente un valor `ALTO`.

Comprueba:

``` text
ALTO = 1
existe_alto = True
```

Explica en qué iteración cambia la bandera.

------------------------------------------------------------------------

# 10. Reto 8 --- Datos mixtos

Utiliza un conjunto que contenga registros:

-   ALTO.
-   NORMAL.
-   BAJO.

Calcula primero manualmente:

1.  Total.
2.  Cantidad ALTO.
3.  Cantidad NORMAL.
4.  Cantidad BAJO.
5.  Suma.
6.  Existencia de ALTO.

Después ejecuta el programa y compara los resultados.

------------------------------------------------------------------------

# 11. Reto 9 --- Detectar un error de inicialización

Analiza:

``` python
for valor in valores:

    contador_altos = 0

    if clasificacion == "ALTO":
        contador_altos += 1
```

### Responde

1.  ¿Qué problema existe?
2.  ¿Por qué el contador no conserva la información?
3.  ¿Dónde debería inicializarse?
4.  Corrige el código.

------------------------------------------------------------------------

# 12. Reto 10 --- Integración con DataLab

Agrega al proyecto una funcionalidad que genere el resumen del
procesamiento.

Debe incluir:

-   Total de registros.
-   Cantidad ALTO.
-   Cantidad NORMAL.
-   Cantidad BAJO.
-   Suma de valores.
-   Bandera de existencia de ALTO.

### Requisito

Utiliza la función existente:

``` python
clasificar_valor(valor)
```

No dupliques la lógica de clasificación.

------------------------------------------------------------------------

# 13. Reto final --- DataLab v0.6

Integra todo lo aprendido.

### Flujo esperado

``` text
Inicio
  ↓
Inicializar variables
  ↓
Procesar registros
  ↓
Contar total
  ↓
Acumular valores
  ↓
Clasificar registro
  ↓
Actualizar contador
  ↓
Actualizar bandera
  ↓
Siguiente registro
  ↓
Mostrar resumen
  ↓
Fin
```

### Resumen mínimo

``` text
===== RESUMEN DATALAB =====

Total de registros:
ALTO:
NORMAL:
BAJO:
Suma de valores:
¿Existe algún ALTO?:
```

------------------------------------------------------------------------

# 14. Casos de prueba

Documenta al menos:

  Caso   Escenario         Resultado esperado
  ------ ----------------- --------------------------------
  1      Todos NORMAL      `ALTO = 0`
  2      Un ALTO           `ALTO = 1`
  3      Varios ALTO       Contador correcto
  4      Todos BAJO        `BAJO = TOTAL`
  5      Datos mixtos      Todos los contadores correctos
  6      Datos conocidos   Suma correcta

Para cada caso registra:

-   Datos utilizados.
-   Resultado esperado.
-   Resultado obtenido.
-   ¿La prueba fue exitosa?

------------------------------------------------------------------------

# 15. Preguntas de reflexión

1.  ¿Cuál es la diferencia entre un contador y un acumulador?
2.  ¿Por qué las variables deben inicializarse antes del ciclo?
3.  ¿Qué problema resuelve una bandera?
4.  ¿Qué ocurre si un contador se reinicia dentro del ciclo?
5.  ¿Cómo verificaste que el resumen es correcto?
6.  ¿Qué relación debe existir entre `ALTO`, `NORMAL`, `BAJO` y `TOTAL`?
7.  ¿Por qué es importante reutilizar `clasificar_valor()`?

------------------------------------------------------------------------

# 16. Entregables

El repositorio debe contener:

-   Código Python de los ejercicios.
-   Implementación integrada en DataLab.
-   Casos de prueba.
-   Resultados de las pruebas.
-   Respuestas de reflexión.
-   Pseudocódigo actualizado.
-   Diagrama de flujo actualizado.
-   Documentación correspondiente.

Todos los cambios deben registrarse mediante Git y publicarse en GitHub.

------------------------------------------------------------------------

# 17. Lista de verificación

-   [ ] Implementé un contador.
-   [ ] Implementé un acumulador.
-   [ ] Implementé una bandera.
-   [ ] Inicialicé las variables antes del ciclo.
-   [ ] Actualicé las variables dentro del ciclo.
-   [ ] Reutilicé `clasificar_valor()`.
-   [ ] Generé un resumen automáticamente.
-   [ ] Verifiqué `ALTO + NORMAL + BAJO = TOTAL`.
-   [ ] Realicé diferentes casos de prueba.
-   [ ] Actualicé pseudocódigo.
-   [ ] Actualicé diagrama de flujo.
-   [ ] Actualicé la documentación.
-   [ ] Realicé commits descriptivos.
-   [ ] Publiqué los cambios en GitHub.
