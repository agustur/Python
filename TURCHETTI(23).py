print ("Mostrar si alguien es mayor o menor de edad")

edad = int(input("\nIngrese su edad: "))

#115 años es la edad de la persona mas longeva del mundo

while edad <= 0 or edad > 115:
    print ("\nError ==> La edad esta fuera de los valores permitidos (1-115)")
    edad = int(input("\nIngrese su edad: "))

if edad >= 18:
    print ("\nEres mayor de edad")
    
else:
    print ("\nEres menor de edad")

#Proyecto: N23
#Autor: Agustin Turchetti
#Fecha: 19/05/2023
#Mensaje: "Realizar un programa que permita ingresar la edad de una persona y muestre MAYOR DE EDAD o MENOR DE EDAD"
