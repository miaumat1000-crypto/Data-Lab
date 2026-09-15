while True:
    registro = input("¿El estudiante se registró a la clase? (si/no)").lower()
    if registro == "no":
        print("El estudiante ha reprobado la materia")
    elif registro == "si":
        nota = float(input("Ingrese la nota del estudiante: "))

        if nota > 5:
            print("Valor erróneo, vuelva a diligenciarlo")

        elif nota < 3:
            print("El estudiante ha reprobado la materia")

        elif nota >= 3 and nota < 4.8:
            print("El estudiante ha aprobado con una nota estándar")

        else:
            print("El estudiante ha aprobado con la máxima calificación")