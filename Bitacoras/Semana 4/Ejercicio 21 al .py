##Ejercicio 21:

def validar_nombre(nombre):
    return len (nombre.strip()) > 0
def validar_correo(correo):
    return "@" in correo and "." in correo
def validar_edad(edad_str):
        if edad_str.isdigit():
            return int(edad_str) > 0
        return False
def validar_valor(valor_str):
     try:
          val=float(valor_str)
          return val >=0
     except ValueError:
          return False


##     
     