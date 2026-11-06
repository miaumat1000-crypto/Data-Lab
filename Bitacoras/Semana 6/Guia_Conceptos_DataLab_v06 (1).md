# Guía de Conceptos: Contadores, Acumuladores y Banderas en DataLab v0.6

## 1. Datos generales

-   **Proyecto integrador:** DataLab
-   **Curso:** Lógica Computacional
-   **Programa:** Ingeniería de Datos e Inteligencia Artificial
-   **Semana:** 6 de 14
-   **Modalidad:** Trabajo individual

## 2. Punto de partida

DataLab ya puede tomar decisiones, validar entradas, procesar múltiples
registros con `for` y mantener un menú repetitivo con `while`.

Ahora aparece una nueva necesidad:

> **¿Cómo puede DataLab recordar lo que ocurrió mientras procesa varios
> registros?**

Los conceptos centrales son:

-   **Contadores**
-   **Acumuladores**
-   **Banderas o variables de estado**

La evolución consiste en pasar de **repetir operaciones** a **mantener
información durante el procesamiento**.

## 3. Procesar y recordar

DataLab debe poder generar un resumen como:

``` text
Registros procesados: 10
ALTO: 3
NORMAL: 5
BAJO: 2
Suma de valores: 487.5
¿Existe algún ALTO?: Sí
```

Para conseguirlo debe conservar información entre iteraciones.

### Preguntas clave

-   ¿Cuántos registros se procesaron?
-   ¿Cuántos pertenecen a una categoría?
-   ¿Cuál es la suma?
-   ¿Ocurrió al menos una situación?
-   ¿Qué información debe mantenerse?

## 4. Contador

Un **contador** permite saber cuántas veces ocurre un evento.

``` python
cantidad_altos = 0

if clasificacion == "ALTO":
    cantidad_altos += 1
```

Características:

-   Normalmente inicia en `0`.
-   Aumenta cuando ocurre el evento.
-   Generalmente aumenta de uno en uno.
-   Su valor final representa la cantidad de eventos.

**Idea clave:** `CONTADOR → ¿Cuántos ocurrieron?`

## 5. Acumulador

Un **acumulador** conserva un resultado progresivo.

``` python
suma_valores = 0
suma_valores += valor
```

Características:

-   Normalmente inicia en `0`.
-   Recibe un nuevo valor en cada iteración.
-   Conserva el resultado acumulado.
-   No necesariamente aumenta de uno en uno.

**Idea clave:** `ACUMULADOR → ¿Cuál es el total acumulado?`

## 6. Contador vs. acumulador

  Característica   Contador         Acumulador
  ---------------- ---------------- --------------------
  Propósito        Contar eventos   Acumular valores
  Valor inicial    `0`              `0`
  Actualización    `+1`             `+ valor`
  Pregunta         ¿Cuántos?        ¿Cuál es el total?

## 7. Bandera o variable de estado

Una **bandera** representa un estado mediante valores booleanos.

``` python
existe_valor_alto = False

if clasificacion == "ALTO":
    existe_valor_alto = True
```

Permite responder:

> **¿Ocurrió alguna situación durante el procesamiento?**

``` text
False → todavía no ocurrió
True  → ya ocurrió
```

La bandera se inicializa antes del ciclo y cambia cuando ocurre el
evento buscado.

## 8. Diseñar las variables antes de programar

  Necesidad              Mecanismo    Ejemplo
  ---------------------- ------------ -----------------------
  Contar registros       Contador     `total = 0`
  Contar una categoría   Contador     `altos = 0`
  Sumar valores          Acumulador   `suma = 0`
  Recordar un evento     Bandera      `existe_alto = False`

Preguntas:

1.  ¿Qué necesito contar?
2.  ¿Qué necesito sumar?
3.  ¿Qué necesito recordar?
4.  ¿Cuál debe ser el valor inicial?
5.  ¿Cuándo se actualiza cada variable?

## 9. Inicialización

Las variables de estado deben inicializarse **antes del ciclo**:

``` python
contador_total = 0
contador_altos = 0
suma_valores = 0
existe_alto = False
```

Si se inicializan dentro del ciclo, pueden perder la información
acumulada.

## 10. Actualización dentro del ciclo

``` python
contador_total += 1
suma_valores += valor

if clasificacion == "ALTO":
    contador_altos += 1
    existe_alto = True
```

Flujo:

``` text
Recibir registro
      ↓
Actualizar total
      ↓
Acumular valor
      ↓
Clasificar
      ↓
Actualizar contador
      ↓
Actualizar bandera si aplica
      ↓
Siguiente registro
```

## 11. Integración con la clasificación

Debe reutilizarse la función existente:

``` python
clasificacion = clasificar_valor(valor)
```

No se debe duplicar innecesariamente la lógica de clasificación.

## 12. Resumen del procesamiento

``` text
Resumen
-------
Total de registros:
ALTO:
NORMAL:
BAJO:
Suma de valores:
¿Existe algún ALTO?:
```

Los resultados deben ser calculados por el programa.

## 13. Consistencia de resultados

Cuando existen tres categorías:

``` text
ALTO + NORMAL + BAJO = TOTAL
```

Ejemplo:

``` text
3 + 5 + 2 = 10
```

Esta relación permite detectar errores en los contadores.

## 14. Ejemplo conceptual

``` python
contador_total = 0
contador_altos = 0
contador_normales = 0
contador_bajos = 0
suma_valores = 0
existe_alto = False

for valor in valores:

    contador_total += 1
    suma_valores += valor

    clasificacion = clasificar_valor(valor)

    if clasificacion == "ALTO":
        contador_altos += 1
        existe_alto = True

    elif clasificacion == "NORMAL":
        contador_normales += 1

    else:
        contador_bajos += 1
```

## 15. Pruebas

Probar:

-   Todos NORMAL.
-   Un ALTO.
-   Varios ALTO.
-   Todos BAJO.
-   Datos mixtos.
-   Un conjunto con suma conocida.

Verificar:

-   Conteo total.
-   Conteo por clasificación.
-   Suma.
-   Bandera.
-   Consistencia entre categorías y total.

## 16. Git y GitHub

Antes:

``` bash
git status
git pull
```

Después:

``` bash
git add src/main.py
git commit -m "feat: agrega resumen del procesamiento"
git push
```

Para documentación:

``` bash
git add docs/
git commit -m "docs: documenta contadores y acumuladores"
git push
```

## 17. Pensamiento crítico

1.  ¿Cuál es la diferencia entre contar y acumular?
2.  ¿Por qué las variables deben inicializarse antes del ciclo?
3.  ¿Qué problema resuelve una bandera?
4.  ¿Qué ocurre si el contador se reinicia dentro del ciclo?
5.  ¿Cómo comprobarías que el resumen es correcto?
6.  ¿Qué información es útil conservar al procesar muchos registros?

## 18. Evolución de DataLab

**DataLab v0.6 --- Procesamiento con estado y resumen**

``` text
DataLab
│
├── Clasificación
├── Selección de operaciones
├── Validación
├── Procesamiento de múltiples registros
├── Menú repetitivo
└── Resumen
    ├── Contadores
    ├── Acumuladores
    └── Banderas
```

Ahora DataLab puede procesar información y **mantener conocimiento sobre
lo ocurrido durante el proceso**.

La siguiente etapa será organizar esta lógica mediante **funciones**,
mejorando la modularidad y reutilización.
