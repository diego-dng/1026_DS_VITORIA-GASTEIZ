import variables

def sumar(num1: float, num2:float):
    """Funcion que suma dos numeros"""
    if type(num1) == str or type(num2) == str:
        return "datos incorrectos"

    v = num1 + num2
    return v

def iniciar_bbdd(url, puerto, pswd):
    if url== "www.bbbdd.com" and puerto == 4321 and pswd == "1234":
        return "conexion bien"
    else:
        return "error de conexion"
