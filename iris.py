#nuevo iris version 3.0 al 2024
from Procesos import Procesos

p = Procesos()
p.MX = int(input("ingrese la cantidad de caracteres en su contraseña: "))
clave = input("ingrese su frase clave: ")
codigo = input("ingrese su codigo de ejecucion: ")
plataforma = input("ingrese su plataforma: ")

contra = p.Viegener(clave,codigo)
for i in codigo:
    if i == "1":
        contra  = p.moduloR(contra)
    elif i == "2":
        contra  = p.moduloC(contra)   
    elif i == "3":
        contra  = p.Fibonazi(contra) 
    elif i == "4":
        contra  = p.baraja(contra)  
    elif i == "5":
        contra  = p.invertir(contra) 
    elif i == "6":
        contra  = p.hop(contra)
    elif i == "7":
        contra  = p.calidad(contra)
    else:
        print("no valido")

contra= p.calidad(contra)

print(f"su contraseña de {p.MX} caracteres es: {contra}") 


