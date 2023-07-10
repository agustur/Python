#Programa: N°9
#Autor: Agustin Turchetti
#Fecha: 28/04/23
#Mensaje: Ingresar el apellido y nombre de una persona, concatenarlos y mostrarlos de 4 distintas formas

print ("Concatenar nombre y apellido y mostrarlos en distinta posicion")

nom = str(input("\nIngrese el nombre: "))
ape = str(input("Ingrese el apellido: "))

AP = ape + " " + nom
NP = nom + " " + ape
APE = ape + ", " + nom
NPH = "Hola " + nom + " " + ape

print ("")
print ("1) ", AP)
print ("2) ", NP)
print ("3) ", APE)
print ("4) ", NPH)
