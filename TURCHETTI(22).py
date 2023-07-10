print (" Sistema de comprobacion de aprobado y reprobado")

nota = float(input("\nIngrese la nota del alumno:"))

while nota <= 0 or nota > 10:
    print ("Error ==> La nota esta fuera de los valores numericos permitidos (1-10)")
    nota = float(input("\nIngrese la nota del alumno:"))

if nota >= 8.50 or nota <= 10:
    print ("El alumno esta aprobado con MUY LOGRADO")
    
elif nota < 8.50 or nota >= 6.50:
    print ("El alumno esta aprobado con LOGRADO")
    
else:
    print ("El alumno esta desaprobado con PENDIENTE")
    
#Proyecto: N22
#Autor: Agustin Turchetti
#Fecha: 12/05/2023
#Mensaje: "Diseñar un programa que permita ingresar el promedio de un alumno y muestre si el alumno está APROBADO o REPROBADO."
