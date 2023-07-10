print ("Ejecicio 36")

cantmen = 0
cantmay = 0

for num in range (1,21,1):
    edad = int(input(f"\nIngrese la edad de la persona N° {num}: "))
    #116 años es la edad de la persona mas vieja del mundo

    while edad < 0 or edad > 116:
        print ("ERROR --> La edad que ingreso no esta entre los valores posible(0-116)")
        edad = int(input(f"\nIngrese la edad de la persona N° {num}: "))

    if edad < 18:
        cantmen = cantmen + 1

    elif edad >= 18:
        cantmay = cantmay + 1

print (f"\nLa cantidad de menores de edad que hay son: {cantmen} y la cantidad de mayores de edad que hay son: {cantmay}")

#Proyecto: N36
#Autor: Agustin Turchetti
#Fecha: 23/06/2023
#Mensaje: "Realizar un programa que permita ingresar la edad de una persona. Al finalizar debe mostrar la cantidad de mayores y menores de edad."