print ("Ingresar 3 notas y mostrar si esta aprobado")

n1 = float(input("\nIngresar la primera nota: "))

while n1 <= 0 or n1 > 10:
    print ("\nERROR ==> La primera nota no esta entre el rango de valores permitidos (1-10)")
    n1 = float(input("\nIngresar la primera nota: "))
    
n2 = float(input("\nIngresar la segunda nota: "))

while n2 <= 0 or n2 > 10:
    print ("\nERROR ==> La segunda nota no esta entre el rango de valores permitidos (1-10)")
    n2 = float(input("\nIngresar la segunda nota: "))
    
n3 = float(input("\nIngresar la tercera nota: "))
while n3 <= 0 or n3 > 10:
    print ("\nERROR ==> La primera nota no esta entre el rango de valores permitidos (1-10)")
    n3 = float(input("\nIngresar la tercera nota: "))

ns= n1 + n2 + n3
nt = ns / 3

if nt >= 6.50 or nt == 10:
    print ("\nEl alumno esta aprobado")
else:
    print ("\nEl alumno esta desaprobado")
           
#Proyecto: N27
#Autor: Agustin Turchetti
#Fecha: 19/05/2023
#Mensaje: "Diseñar un programa que permita ingresar tres notas, calcule el promedio y muestre si está APROBADO o DESAPROBADO."
