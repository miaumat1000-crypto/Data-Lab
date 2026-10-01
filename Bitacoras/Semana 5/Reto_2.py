## 🧩 Reto 2: El Procesador de Lotes (Uso de `for`)
**Contexto:** DataLab recibe un "lote" de 10 sensores de temperatura.
**Objetivo:** Implementar un ciclo for que simule la lectura de estos 10 sensores. Por cada lectura, el programa debe imprimir: *"Sensor [N]: Temperatura procesada"*. Al final, debe imprimir un mensaje de *"Lote completo"*

# Simulando la lectura de un lote de 10 sensores
for i in range(1, 11):
    print(f"Sensor {i}: Temperatura procesada")

print("Lote completo")

