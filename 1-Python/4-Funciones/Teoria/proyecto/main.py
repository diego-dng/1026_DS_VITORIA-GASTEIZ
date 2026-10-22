#import funciones
#import variables

from funciones import iniciar_bbdd
from variables import url, puerto, pswd
print("hola")

"""res = funciones.sumar(variables.n1, variables.n2)
print(res)
"""
res_2 = iniciar_bbdd(url, puerto, pswd)
print(res_2)