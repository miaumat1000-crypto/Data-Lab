# Guía de Conceptos: Evolución de DataLab v0.5
## De Procesamiento Fijo a Interacción Dinámica

Esta guía detalla la transición de **DataLab** hacia una aplicación interactiva, permitiendo que el procesamiento de datos no sea una ejecución lineal, sino un servicio continuo controlado por el usuario.

### 1. El Cambio de Paradigma: `for` vs `while`

En el desarrollo de DataLab, hemos pasado de procesar datos en bloques cerrados a procesarlos bajo demanda.

| Estructura | Uso en DataLab | Naturaleza | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Ciclo `for`** | Procesar un archivo con $N$ registros conocidos. | **Determinista** (Sabemos el final). | "Procesar los 50 registros del CSV". |
| **Ciclo `while`** | Mantener el menú activo hasta que el usuario decida salir. | **Condicional** (Depende de un evento). | "Repetir menú mientras `opcion != 'salir'`". |

### 2. Anatomía del Ciclo `while`

Para que DataLab funcione correctamente, todo ciclo `while` debe tener tres elementos:
1. **Condición de Entrada:** Una expresión booleana que define si el ciclo comienza o continúa.
2. **Cuerpo del Ciclo:** Las acciones que se repiten (Menú $\rightarrow$ Selección $\rightarrow$ Ejecución).
3. **Actualización del Estado:** Una acción dentro del cuerpo que modifique la condición. **Sin esto, DataLab entraría en un "Ciclo Infinito", bloqueando la computadora.**

### 3. Simulación de `do-while` en Python

Dado que Python no posee un `do-while` nativo, en DataLab implementamos la lógica de **"Ejecutar primero, preguntar después"**. Esto es vital para que el menú se muestre al menos una vez sin necesidad de inicializar variables externas complejas.

**Lógica implementada:**
`while True` $\rightarrow$ `Ejecución de código` $\rightarrow$ `Evaluación de salida` $\rightarrow$ `break`.

---

## 📊 Representación Visual de Flujos

A continuación se describe la lógica de los diagramas de flujo para estas estructuras:

### A. Ciclo `for` (Iterativo)
`[Inicio]` $\rightarrow$ `[¿Quedan elementos en la secuencia?]` $\rightarrow$ (Sí) $\rightarrow$ `[Ejecutar cuerpo]` $\rightarrow$ `[Siguiente elemento]` $\rightarrow$ (Vuelta al inicio) $\rightarrow$ (No) $\rightarrow$ `[Fin]`.

### B. Ciclo `while` (Pre-condición)
`[Inicio]` $\rightarrow$ `[¿Se cumple la condición?]` $\rightarrow$ (Sí) $\rightarrow$ `[Ejecutar cuerpo]` $\rightarrow$ `[Actualizar estado]` $\rightarrow$ (Vuelta a la condición) $\rightarrow$ (No) $\rightarrow$ `[Fin]`.

### C. Ciclo `do-while` (Post-condición)
`[Inicio]` $\rightarrow$ `[Ejecutar cuerpo]` $\rightarrow$ `[¿Se cumple la condición de salida?]` $\rightarrow$ (No) $\rightarrow$ (Vuelta al cuerpo) $\rightarrow$ (Sí) $\rightarrow$ `[Fin]`.
