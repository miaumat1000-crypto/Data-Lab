# Guía del estudiante — Semana 2

**Proyecto integrador:** DataLab  
**Curso:** Lógica Computacional  
**Semana:** 2 de 14  
**Modalidad:** Trabajo individual

---

# 1. Reto de la semana

En la Semana 1 DataLab aprendió a procesar un registro.

Ahora debe aprender a **tomar decisiones**.

Tu reto es transformar una regla de negocio en:

**Regla → condición → pseudocódigo → diagrama → Python → prueba → commit**

---

# 2. Concepto central

Una estructura condicional permite que un programa tome diferentes caminos dependiendo de una condición.

En Python utilizaremos:

```python
if
elif
else
```

No memorices solamente la sintaxis.

Debes poder explicar:

- ¿Qué significa una condición?
- ¿Qué ocurre cuando es verdadera?
- ¿Qué ocurre cuando es falsa?
- ¿Por qué puede haber varias alternativas?

---

# 3. Actividad Feynman

Explica esta situación sin utilizar código:

> DataLab recibe un valor y debe determinar si está por debajo, dentro o por encima de un rango esperado.

Explícalo como si la persona que te escucha nunca hubiera programado.

Después responde:

1. ¿Cuántos caminos existen?
2. ¿Qué condición permite seleccionar cada camino?
3. ¿Qué ocurre si el valor está exactamente en el límite?

---

# 4. Diseñar antes de programar

Define:

### Entrada

¿Qué dato recibe DataLab?

### Reglas

¿Qué condiciones debe evaluar?

### Salidas

¿Qué clasificación debe producir?

---

# 5. Pseudocódigo

Construye una solución similar conceptualmente a:

```text
INICIO

    Leer valor

    SI valor está por debajo del límite inferior
        Clasificar como BAJO
    SINO SI valor está por encima del límite superior
        Clasificar como ALTO
    SINO
        Clasificar como NORMAL

    Mostrar clasificación

FIN
```

Adapta el algoritmo al problema concreto de DataLab.

---

# 6. Diagrama de flujo

Actualiza el diagrama de la Semana 1.

Debe mostrar claramente:

```text
              ¿Condición 1?
               /        \
             Sí          No
             ↓            ↓
         Acción 1     ¿Condición 2?
                       /       \
                     Sí         No
                     ↓           ↓
                  Acción 2    Acción 3
```

---

# 7. Laboratorio — Recuperar DataLab

Antes de modificar el código:

```bash
git status
git pull
```

Comprueba que tienes la versión anterior del proyecto.

---

# 8. Implementar `if`, `elif`, `else`

Ejemplo:

```python
if valor < limite_inferior:
    clasificacion = "BAJO"
elif valor > limite_superior:
    clasificacion = "ALTO"
else:
    clasificacion = "NORMAL"
```

No copies el ejemplo sin comprenderlo.

Explica qué sucedería si:

- `valor` es menor que el límite.
- `valor` es igual al límite.
- `valor` está entre los límites.
- `valor` supera el límite.

---

# 9. Probar DataLab

Realiza mínimo cuatro pruebas:

| Caso | Entrada | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| Bajo | | | |
| Límite | | | |
| Normal | | | |
| Alto | | | |

Los casos de frontera son importantes.

---

# 10. Reto individual

Agrega una segunda regla relacionada con el contexto de DataLab.

Debes realizar el ciclo completo:

1. Definir la regla.
2. Actualizar el pseudocódigo.
3. Actualizar el diagrama.
4. Modificar Python.
5. Probar.
6. Documentar.
7. Crear un commit.
8. Hacer `push`.

---

# 11. Git y GitHub

Antes de comenzar:

```bash
git status
git pull
```

Después de modificar el proyecto:

```bash
git status
git add .
git commit -m "feat: agrega clasificacion por reglas"
git push
```

Si también modificaste documentación:

```bash
git add docs/
git commit -m "docs: actualiza algoritmo de clasificacion"
git push
```

Los mensajes deben describir lo que realmente cambiaste.

---

# 12. Entregable

Tu repositorio debe contener:

- [ ] Código actualizado.
- [ ] Pseudocódigo actualizado.
- [ ] Diagrama actualizado.
- [ ] Pruebas de los diferentes caminos.
- [ ] Nueva funcionalidad integrada a DataLab.
- [ ] Commits descriptivos.
- [ ] Cambios publicados en GitHub.

---

# 13. Criterios de finalización

Antes de entregar, verifica:

- [ ] Puedo explicar qué es una condición.
- [ ] Puedo explicar `if`.
- [ ] Puedo explicar `elif`.
- [ ] Puedo explicar `else`.
- [ ] Mi algoritmo contempla todos los caminos.
- [ ] Probé los valores límite.
- [ ] Mi código corresponde al pseudocódigo.
- [ ] Mi diagrama corresponde al código.
- [ ] No eliminé accidentalmente la funcionalidad de la Semana 1.
- [ ] Mi repositorio está actualizado.
- [ ] Puedo explicar mi solución sin leer el código.

---

# 14. Reflexión final

Responde:

1. ¿Por qué no es suficiente probar únicamente un valor normal?
2. ¿Qué diferencia existe entre una condición y una acción?
3. ¿Qué sucede si las condiciones están en un orden incorrecto?
4. ¿Qué ventaja tiene representar primero la decisión mediante un diagrama?
5. ¿Qué cambió en DataLab respecto a la Semana 1?
