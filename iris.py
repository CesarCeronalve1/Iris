#nuevo iris version 3.0 al 2024
from Procesos import Procesos

class iris:

    version = "3.0.4"
    p = Procesos()
    archivo =""
    datos =""
    clave =""
    codigo=""
    plataforma=""

    def leer_datos_archivo(self,ruta_archivo):
        datos = {}
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                clave, valor = linea.strip().split(':')
                datos[clave] = valor
        return datos
    
    def inicio(self):
        print(f"Iris version: {self.version}")
        self.p.MX = int(input("ingrese la cantidad de caracteres: "))
        print("Tiene un archivo con sus datos?")
        print("1.- si")
        print("2.-No")
        men = input("")
        if men == "1":
            self.archivo = input("ingresa el nombre del archivo: ")




            self.datos = self.leer_datos_archivo(f"{self.archivo}")
            self.clave = self.datos.get('clave')
            self.codigo = self.datos.get('codigo')
            self.plataforma = input("ingrese su plataforma: ")
            self.programa()
        elif men == "2":
            self.clave = input("ingrese su clave: ")
            self.codigo = input("ingrese su codigo EJX: ")
            self.plataforma = input("ingrese su plataforma: ")
            self.programa()
        else:
            print("Respuesta incorrecta")
            self.inicio()


    def programa(self):
        self.contra = self.p.Viegener(self.clave,self.plataforma)
        # print(contra)
        for i in self.codigo:
            if i == "1":
                self.contra  = self.p.moduloR(self.contra)
                # print(f"1: {contra}")
            elif i == "2":
                self.contra  = self.p.moduloC(self.contra)  
                # print(f"2: {contra}") 
            elif i == "3":
                self.contra  = self.p.Fibonazi(self.contra) 
                # print(f"3: {contra}")
            elif i == "4":
                self.contra  = self.p.baraja(self.contra)
                # print(f"4: {contra}")
            elif i == "5":
                self.contra  = self.p.invertir(self.contra)
                # print(f"5: {contra}") 
            elif i == "6":
                self.contra  = self.p.hop(self.contra)
                # print(f"6: {contra}")
            elif i == "7":
                self.contra  = self.p.calidad(self.contra)
                # print(f"7: {contra}")
            else:
                print("no valido")
        self.contra = self.p.calidad(self.contra)
        print(f"su contraseña de {self.p.MX} caracteres es: {self.contra}") 

if __name__ == "__main__":
    i = iris()
    i.inicio()



