print ("Transformador de horas y minutos")

m = int(input("\nIngrese la cantidad de minutos: "))

while m < 0:
    print ("Error, el valor esta en negativo")
    m = int(input("\nIngrese la cantidad de minutos: "))

horas = m // 60
minutos = m % 60

print ("\nEquivale a "+str(horas)+" hs"+" y "+str(minutos)+" min")

#Proyecto: N20
#Autor: Agustin Turchetti
#Fecha: 12/05/2023
#Mensaje: "Diseñar un programa que permita ingresar un valor en minutos. Debe mostrar la cantidad de horas y minutos que equivale."