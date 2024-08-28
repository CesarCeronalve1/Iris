#nuevo iris version 3.0 al 2024
from Procesos import Procesos
version = "3.0.4"
p = Procesos()
print(f"Iris version: {version}")
p.MX = int(input("ingrese la cantidad de caracteres: "))
# clave = input("ingrese su clave: ")
# codigo = input("ingrese su codigo EJX: ")
# plataforma = input("ingrese su plataforma: ")

def leer_datos_archivo(ruta_archivo):
    datos = {}
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            clave, valor = linea.strip().split(':')
            datos[clave] = valor
    return datos
datos = leer_datos_archivo("Data.txt")
clave = datos.get('clave')
codigo = datos.get('codigo')
plataforma = input("ingrese su plataforma: ")

contra = p.Viegener(clave,plataforma)
# print(contra)
for i in codigo:
    if i == "1":
        contra  = p.moduloR(contra)
        # print(f"1: {contra}")
    elif i == "2":
        contra  = p.moduloC(contra)  
        # print(f"2: {contra}") 
    elif i == "3":
        contra  = p.Fibonazi(contra) 
        # print(f"3: {contra}")
    elif i == "4":
        contra  = p.baraja(contra)
        # print(f"4: {contra}")
    elif i == "5":
        contra  = p.invertir(contra)
        # print(f"5: {contra}") 
    elif i == "6":
        contra  = p.hop(contra)
        # print(f"6: {contra}")
    elif i == "7":
        contra  = p.calidad(contra)
        # print(f"7: {contra}")
    else:
        print("no valido")

contra = p.calidad(contra)

print(f"su contraseña de {p.MX} caracteres es: {contra}") 


