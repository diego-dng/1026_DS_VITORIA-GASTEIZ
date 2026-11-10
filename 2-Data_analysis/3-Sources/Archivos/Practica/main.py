import funciones as f
import os 
from clase import Fichero
#os.chdir("C:\\Users\\Diego Nuñez\\Desktop\\car_ejercicio")

res_ruta = f.ruta_inicial()
res = f.crear_carpetas(res_ruta)



for i in os.listdir():
    if not os.path.isdir(res_ruta + "\\" + i):
        continue

    fichero = Fichero(res_ruta, i)
    fichero.colocar()

    
