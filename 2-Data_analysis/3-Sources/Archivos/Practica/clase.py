import os 
import shutil
import variables as v

class Fichero:

    doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
    img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
    software_types = ('.exe', '.py','.ipynb')

    ruta = os.getcwd()

    def __init__(self, ruta, archivo):
        self.ruta = ruta
        self.archivo = archivo


    def colocar(self):
        # colocar el obketo fichero en la carpeta que toca.
        for archivo in os.listdir():
                print(archivo)
                if not os.path.isfile(self.ruta+ "\\" + archivo):
                    print("es una carpeta")
                    continue
        
                if archivo.lower().endswith(self.doc_types):
                    print("es un documento")
                    print(self.ruta + "\\" + archivo)
                    shutil.move(self.ruta + "\\" + archivo, self.ruta + "\\" + "Documentos")
                elif archivo.lower().endswith(self.img_types):
                    print("es un imagenes")
                    print(self.ruta + "\\" + archivo)
                    shutil.move(self.ruta + "\\" + archivo, self.ruta + "\\" + "Imagenes")
                elif archivo.lower().endswith(self.software_types):
                    print("es un software")
                    print(self.ruta + "\\" + archivo)
                    shutil.move(self.ruta + "\\" + archivo, self.ruta + "\\" + "Software")
                else:
                    shutil.move(self.ruta + "\\" + archivo, self.ruta + "\\" + "Otros")