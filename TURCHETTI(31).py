print ("Ejercicio 31")

num = int(input("Ingrese el numero del frasco: "))

while num <= 0 or num > 3:
    print ("ERROR ==> El numero que ingreso no esta en los valores que se permiten, ingrese uno que este entre los siguientes valores(1-3)")
    num = int(input("Ingrese el numero del frasco: "))

if num == 1:
    print ("El tamaño del frasco es chico")

elif num == 2:
    print ("El tamaño del frasco es mediano")

else:
    print ("El tamaño del frasco es grande")

#Proyecto: N31
#Autor: Agustin Turchetti
#Fecha: 16/06/2023
#Mensaje: "Realizar un programa que permita ingresar el número del frasco y muestre el tamaño"