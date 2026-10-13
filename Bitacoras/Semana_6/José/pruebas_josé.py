class AnalizadorCaso:

  def __init__(self, nombre, valores):
    self.nombre = nombre
    self.valores = [float(v) for v in valores]
    self._procesar_datos()

  def _clasificar_valor(self, valor):
    if valor > 60.0:
      return "Alto"
    elif valor >= 40.0:
      return "Normal"
    else:
      return "Bajo"

  def _procesar_datos(self):
    self.total_registros = len(self.valores)
    self.suma_valores = sum(self.valores)

    # Clasificamos cada valor usando list comprehensions
    clasificaciones = [self._clasificar_valor(v) for v in self.valores]

    # Contamos las ocurrencias de cada categoría
    self.contador_altos = clasificaciones.count("Alto")
    self.contador_normales = clasificaciones.count("Normal")
    self.contador_bajos = clasificaciones.count("Bajo")
    self.existe_alto = self.contador_altos > 0

  def mostrar_reporte(self):
    print(f"--- {self.nombre} ---")
    print(f"Datos: {self.valores}")
    print(f"Resultados Total: {self.total_registros}")
    print(f"Alto: {self.contador_altos}")
    print(f"Normal: {self.contador_normales}")
    print(f"Bajo: {self.contador_bajos}")
    print(f"Suma: {self.suma_valores}")
    print(f"Existe ALTO: {self.existe_alto}\n")


# Ejecución de los 6 casos de prueba instanciando la clase
AnalizadorCaso(
    "Caso 1: Todos NORMAL", [45.0, 50.0, 55.0]
).mostrar_reporte()
AnalizadorCaso("Caso 2: Un ALTO", [45.0, 75.0, 50.0]).mostrar_reporte()
AnalizadorCaso("Caso 3: Varios ALTO", [65.0, 80.0, 45.0]).mostrar_reporte()
AnalizadorCaso("Caso 4: Todos BAJO", [10.0, 20.0, 30.0]).mostrar_reporte()
AnalizadorCaso(
    "Caso 5: Datos mixtos", [22.5, 55.1, 72.3, 38.7, 61.4]
).mostrar_reporte()
AnalizadorCaso("Caso 6: Datos conocidos", [10, 20, 30, 40, 50]).mostrar_reporte()