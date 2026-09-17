    # Solicitar datos del usuario
while True:
    tipo_documento = input("Ingrese el tipo de documento (CC / TI): ").strip().upper()

    match tipo_documento: 
        case "CC":
            print("Tipo de documento: Cédula de ciudadanía.")
            print("Estado: Mayor de edad.")
        case "TI":
            print("Tipo de documento: Tarjeta de Identidad.")
            print("Estado: Menor de edad.")
        case _:
            print("Tipo de documento no reconocido. Use CC para cédula o TI para tarjeta de identidad.")