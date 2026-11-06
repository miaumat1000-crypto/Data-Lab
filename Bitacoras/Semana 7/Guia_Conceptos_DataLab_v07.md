# Guía de Conceptos: Funciones y Modularización en DataLab v0.7

## 1. Datos generales

- **Proyecto integrador:** DataLab
- **Curso:** Lógica Computacional
- **Programa:** Ingeniería de Datos e Inteligencia Artificial
- **Semana:** 7 de 14
- **Modalidad:** Trabajo individual

## 2. Punto de partida

DataLab ya puede tomar decisiones, validar entradas, procesar múltiples
registros mediante `for` y `while`, mantener información mediante
contadores, acumuladores y banderas, y generar un resumen.

Ahora aparece una nueva necesidad:

> **¿Cómo podemos organizar el programa para que cada parte tenga una
> responsabilidad clara, pueda reutilizarse y sea más fácil de probar?**

Los conceptos centrales de esta semana son:

- **Funciones**
- **Parámetros**
- **Argumentos**
- **Valores de retorno**
- **Alcance básico de variables**
- **Modularización**
- **Refactorización**

La evolución consiste en pasar de tener lógica concentrada en `main()` a
organizar el programa mediante unidades de comportamiento con
responsabilidades claras.

---

## 3. ¿Qué es una función?

Una función es una unidad de comportamiento reutilizable que realiza una
tarea específica.

Una función permite:

- Organizar el código.
- Evitar duplicación.
- Reutilizar una operación.
- Probar una tarea de manera independiente.
- Facilitar la lectura y mantenimiento del programa.

Una función debe responder, idealmente, a tres preguntas:

1. ¿Qué recibe?
2. ¿Qué hace?
3. ¿Qué produce?

### Ejemplo

```python
def mostrar_mensaje():
    print("DataLab")
```

Para utilizarla:

```python
mostrar_mensaje()
```

La función puede ejecutarse nuevamente sin escribir otra vez la instrucción
que contiene.

---

## 4. Definir e invocar una función

Existen dos acciones diferentes:

### Definir

Crear la función y establecer lo que hará.

```python
def mostrar_mensaje():
    print("DataLab")
```

### Invocar

Ejecutar una función que ya fue definida.

```python
mostrar_mensaje()
```

### Idea clave

```text
definir  → crear la función
invocar  → ejecutar la función
```

Definir una función no significa ejecutarla automáticamente.

---

## 5. Responsabilidad de una función

No se trata de crear muchas funciones simplemente para dividir el código.

La pregunta correcta es:

> **¿Qué responsabilidad tiene este bloque y puede expresarse como una
> unidad independiente?**

Una función debe tener una responsabilidad comprensible.

Ejemplos dentro de DataLab:

```text
mostrar_menu()
leer_opcion()
clasificar_valor()
procesar_registros()
mostrar_resumen()
ejecutar_opcion()
```

Cada función representa una tarea que puede explicarse con claridad.

---

## 6. Parámetros

Un parámetro es una variable definida en la función para recibir
información.

Ejemplo:

```python
def saludar(nombre):
    print(f"Hola {nombre}")
```

En este caso:

```text
nombre → parámetro
```

La función está preparada para recibir un dato que utilizará durante su
ejecución.

---

## 7. Argumentos

Un argumento es el valor que se envía a una función cuando se invoca.

```python
saludar("Ana")
```

En este caso:

```text
nombre → parámetro
"Ana"  → argumento
```

### Modelo mental

```text
def saludar(nombre):
          ↑
      parámetro

saludar("Ana")
        ↑
     argumento
```

### Regla

```text
Parámetro → aparece en la definición.
Argumento → aparece en la llamada.
```

---

## 8. Parámetros y reutilización

Los parámetros permiten utilizar una misma función con diferentes valores.

```python
def saludar(nombre):
    print(f"Hola {nombre}")
```

Se puede utilizar varias veces:

```python
saludar("Ana")
saludar("Carlos")
saludar("María")
```

La función es la misma, pero recibe argumentos diferentes.

Esto reduce la necesidad de duplicar código.

---

## 9. Valores de retorno

Una función puede producir un resultado mediante `return`.

Ejemplo:

```python
def duplicar(valor):
    return valor * 2
```

Uso:

```python
resultado = duplicar(5)
```

Después de la ejecución:

```text
resultado = 10
```

### Idea clave

`return` permite que una función entregue un resultado al bloque que la
invocó.

---

## 10. ¿Qué ocurre con `return`?

Consideremos:

```python
def duplicar(valor):
    return valor * 2
```

La función:

1. Recibe un valor.
2. Calcula el doble.
3. Retorna el resultado.

```text
duplicar(5)
     ↓
  5 * 2
     ↓
 return 10
     ↓
resultado = 10
```

El resultado puede utilizarse posteriormente.

---

## 11. `print()` frente a `return`

No cumplen la misma función.

### `print()`

Muestra información en pantalla:

```python
def mostrar_clasificacion(clasificacion):
    print(clasificacion)
```

### `return`

Entrega información al código que llamó a la función:

```python
def obtener_clasificacion(valor):
    return clasificacion
```

### Diferencia fundamental

```text
print() → presenta información.
return  → entrega información.
```

Una función que debe producir un valor reutilizable normalmente debe
retornarlo.

---

## 12. Funciones con efecto

Una función puede realizar una acción sin retornar un valor que vaya a ser
utilizado posteriormente.

Ejemplo:

```python
def mostrar_resumen():
    print("Resumen de DataLab")
```

Su responsabilidad es producir un efecto visible:

```text
mostrar información
```

Este tipo de función puede ser apropiado cuando la tarea consiste
precisamente en presentar información.

---

## 13. Funciones que retornan valores

Otra función puede calcular o producir un resultado.

Ejemplo:

```python
def calcular_total(valores):
    total = 0

    for valor in valores:
        total += valor

    return total
```

Su resultado puede utilizarse:

```python
total = calcular_total(valores)
```

### Idea clave

```text
Función con efecto → realiza una acción.
Función con retorno → produce un resultado reutilizable.
```

La elección depende de la responsabilidad de la función.

---

## 14. Alcance básico de variables

Una función puede trabajar con variables locales.

Ejemplo:

```python
def calcular():
    resultado = 10
    return resultado
```

La variable `resultado` pertenece al contexto de la función.

Esto permite mantener información localizada y evitar dependencias
innecesarias.

### Regla de diseño

> Siempre que sea posible, pasa información mediante parámetros y devuelve
> resultados mediante `return`.

---

## 15. Variables globales

Una variable global puede ser utilizada desde diferentes partes del
programa.

Sin embargo, utilizar variables globales para transportar información
entre funciones puede generar dependencias difíciles de comprender.

Ejemplo conceptual:

```text
función A
   ↓
modifica variable global
   ↓
función B
   ↓
depende de esa variable
```

Esto puede dificultar:

- Entender el código.
- Probar funciones.
- Reutilizar funciones.
- Detectar errores.

### Regla de trabajo

Evitar variables globales para comunicar información entre funciones salvo
que exista una razón explícita.

---

## 16. Modularización

Modularizar significa dividir una solución en componentes más pequeños y
organizados.

En esta semana la modularización se trabajará principalmente mediante
funciones.

En lugar de concentrar toda la lógica:

```text
main()
 ├── menú
 ├── validación
 ├── procesamiento
 ├── clasificación
 ├── resumen
 └── salida
```

se busca una organización como:

```text
main()
 ├── mostrar_menu()
 ├── leer_opcion()
 ├── ejecutar_opcion()
 │     ├── procesar_registros()
 │     │      └── clasificar_valor()
 │     └── mostrar_informacion()
 └── controlar_salida()
```

La estructura exacta puede variar.

Lo importante es que cada función tenga una responsabilidad comprensible.

---

## 17. ¿Qué es refactorizar?

Refactorizar consiste en mejorar la estructura interna del código sin
cambiar su comportamiento esperado.

El objetivo de esta semana no es agregar una funcionalidad grande.

El objetivo es:

```text
Código funcionando
       ↓
Refactorización
       ↓
Mismo comportamiento
+ mejor organización
+ menor duplicación
+ mayor reutilización
```

---

## 18. Refactorización en DataLab

DataLab puede tener lógica concentrada en `main.py`.

La refactorización busca separar responsabilidades.

Una estructura posible:

```text
main()
 ├── mostrar_menu()
 ├── leer_opcion()
 ├── ejecutar_opcion()
 │     └── procesar_registros()
 │            └── clasificar_valor()
 └── mostrar_resumen()
```

`main()` pasa a ser principalmente un coordinador.

Las tareas específicas quedan encapsuladas en funciones.

---

## 19. `clasificar_valor()` como función reutilizable

DataLab ya dispone de una lógica de clasificación.

La función debe recibir el valor y retornar su clasificación:

```python
def clasificar_valor(valor):
    # lógica de clasificación
    return clasificacion
```

Uso:

```python
clasificacion = clasificar_valor(valor)
```

La ventaja es que diferentes partes del programa pueden utilizar la misma
lógica sin duplicarla.

### Principio

> Si una operación ya está implementada como función reutilizable, no se
> debe duplicar su lógica en otros lugares.

---

## 20. `procesar_registros()`

La responsabilidad de procesar una cantidad de registros puede separarse
del control del menú.

Conceptualmente:

```python
def procesar_registros(cantidad):
    # procesamiento de registros
    # actualización de resultados
    return resultado
```

La función recibe la información necesaria y puede retornar los resultados
que deban ser utilizados por otras partes del programa.

---

## 21. `mostrar_menu()`

La función `mostrar_menu()` debe encargarse de presentar las opciones.

Por ejemplo:

```python
def mostrar_menu():
    print("1. Procesar registros")
    print("2. Mostrar información")
    print("3. Salir")
```

Su responsabilidad es presentar el menú.

No debería contener toda la lógica de procesamiento de DataLab.

---

## 22. `main()` como coordinador

La función `main()` debe actuar como coordinador general.

Una posible organización:

```python
def main():
    mostrar_menu()
    opcion = leer_opcion()
    ejecutar_opcion(opcion)
```

La idea no es que `main()` desaparezca.

La idea es evitar que contenga toda la lógica del programa.

### Principio

```text
main() → coordina
funciones → realizan tareas específicas
```

---

## 23. Reutilización

Una función es especialmente útil cuando una tarea puede utilizarse más de
una vez.

Ejemplo:

```python
def validar_nota(nota):
    ...
```

Puede ser utilizada desde diferentes partes del programa.

Sin función:

```text
bloque de validación A
bloque de validación B
bloque de validación C
```

Con función:

```text
validar_nota()
      ↑
 ┌────┼────┐
 A    B    C
```

La lógica queda centralizada.

---

## 24. Pruebas independientes

Una función bien definida puede probarse de manera más independiente.

Ejemplo:

```python
def duplicar(valor):
    return valor * 2
```

Pruebas:

```python
duplicar(5)   # 10
duplicar(0)   # 0
duplicar(-2)  # -4
```

Esto permite identificar errores en una tarea concreta.

---

## 25. Pruebas antes y después

La refactorización puede modificar muchas partes internas del programa.

Por eso se deben ejecutar pruebas antes de comenzar.

Registrar resultados de:

- Clasificación.
- Procesamiento.
- Resumen.
- Opciones válidas.
- Opciones inválidas.
- Salida del programa.

Después de refactorizar, ejecutar las mismas pruebas.

### Objetivo

```text
Antes → Resultado A
Refactorización
Después → Resultado A
```

El comportamiento esperado debe mantenerse.

---

## 26. Errores frecuentes

### Crear funciones demasiado grandes

Una función que contiene demasiadas responsabilidades puede ser difícil
de comprender.

### Crear funciones sin responsabilidad clara

Dividir código sin una razón no mejora necesariamente el diseño.

### Depender de variables globales

Las dependencias ocultas dificultan la reutilización y las pruebas.

### Utilizar `print()` cuando se necesita un resultado

Si otro bloque necesita utilizar el valor, debe considerarse `return`.

### Confundir parámetros y argumentos

Recordar:

```text
parámetro → definición
argumento → llamada
```

### Cambiar el comportamiento durante la refactorización

La estructura puede cambiar, pero el comportamiento esperado debe mantenerse.

### No probar después de modificar

Toda modificación estructural debe verificarse.

---

## 27. Checklist conceptual

Antes de finalizar la Semana 7, debo poder explicar:

- [ ] Qué es una función.
- [ ] Cómo se define una función.
- [ ] Cómo se invoca una función.
- [ ] Qué es un parámetro.
- [ ] Qué es un argumento.
- [ ] Qué hace `return`.
- [ ] Diferencia entre `print()` y `return`.
- [ ] Qué es una variable local.
- [ ] Por qué evitar dependencias globales innecesarias.
- [ ] Qué significa modularizar.
- [ ] Qué significa refactorizar.
- [ ] Por qué `main()` debe actuar principalmente como coordinador.

---

## 28. Evolución de DataLab

### DataLab v0.6

```text
Procesar
   ↓
Contar
   ↓
Acumular
   ↓
Recordar estados
   ↓
Generar resumen
```

### DataLab v0.7

```text
Coordinar
   ↓
Delegar tareas
   ↓
Reutilizar funciones
   ↓
Procesar
   ↓
Retornar resultados
   ↓
Mantener el resumen
```

La funcionalidad anterior se conserva, pero la estructura interna mejora.

---

## 29. Conexión con la Semana 8

La modularización realizada en esta semana será la base para trabajar con
**estructuras de datos**.

Las funciones permitirán que el programa procese conjuntos de información
de manera más organizada.

La evolución será:

```text
Semana 6
Estado y resumen
       ↓
Semana 7
Funciones y modularización
       ↓
Semana 8
Estructuras de datos
```
