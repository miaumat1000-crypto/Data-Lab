
while True:


 
    Nota = float(input("Ingrese la nota del estudiante: "))

    
    match Nota:
        case a if 0 < a < 3.5:
                print("El estudiante ha reprobado")

        case b if 3.5 <= b < 4.8:
                print("El estudiante ha aprovado con la nota estandar")

        case c if 4.8 <= c <= 5:
                print("El estudiante ha aprovado con la nota maxima")

        case _:
                print("dato invalido papu :<")