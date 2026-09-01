"""DataLab - Semana 1
Primera implementación del proyecto integrador.
"""

def main():
    print("=== DataLab | Semana 1 ===")
    print("Primera versión del procesamiento de un registro.")

    registro_id = input("Ingrese el identificador del registro: ")
    valor = float(input("Ingrese el valor del registro: "))

    # Regla inicial de ejemplo:
    # un valor >= 50 se considera "alto"; de lo contrario, "normal".
    # Esta regla deberá corresponder al algoritmo diseñado por el estudiante.
    if valor >= 50:
        clasificacion = "ALTO"
    else:
        clasificacion = "NORMAL"

    print("\nResultado")
    print(f"Registro: {registro_id}")
    print(f"Valor: {valor}")
    print(f"Clasificación: {clasificacion}")


if __name__ == "__main__":
    main()
