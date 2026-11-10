import os
import shutil
import variables as v

def ruta_inicial():
    os.chdir("C:\\Users\\Diego Nuñez\\Desktop\\car_ejercicio")
    ruta_carpeta = os.getcwd()
    return ruta_carpeta

def crear_carpetas(ruta):
    print("ruta crear carpetas ", ruta)
    print(v.lista_carpetas)
    for i in v.lista_carpetas:
        #print(ruta + "\\" + i)
        os.makedirs(ruta + "\\" + i, exist_ok= True)
    
    return True


def colocar(ruta):
    print(os.getcwd())
    for archivo in os.listdir():
        print(archivo)
        if not os.path.isfile(ruta+ "\\" + archivo):
            print("es una carpeta")
            continue

        if archivo.lower().endswith(v.doc_types):
            print("es un documento")
            print(ruta + "\\" + archivo)
            shutil.move(ruta + "\\" + archivo, ruta + "\\" + "Documentos")
        elif archivo.lower().endswith(v.img_types):
            print("es un imagenes")
            print(ruta + "\\" + archivo)
            shutil.move(ruta + "\\" + archivo, ruta + "\\" + "Imagenes")
        elif archivo.lower().endswith(v.software_types):
            print("es un software")
            print(ruta + "\\" + archivo)
            shutil.move(ruta + "\\" + archivo, ruta + "\\" + "Software")
        else:
            shutil.move(ruta + "\\" + archivo, ruta + "\\" + "Otros")

    return True