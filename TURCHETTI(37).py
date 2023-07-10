print ("Ejercicio 37")

cant_aprobado = 0
cant_desaprobado = 0

for alumcon in range (1, 11, 1):
    nota1 = int(input(f"\nIngrese la nota N°1 del alumno N°{alumcon}: "))
    while nota1 < 1 or nota1 > 10 :
        print ("ERROR --> La nota N°1 es menor a 0 o mayor a 10")
        nota1 = int(input(f"\nIngrese de nuevo la nota N°1 del alumno N°{alumcon}: "))

    nota2 = int(input(f"Ingrese la nota N°2 del alumno N°{alumcon}: "))
    while nota2 < 1 or nota2 > 10 :
        print ("ERROR --> La nota N°2 es menor a 0 o mayor a 10")
        nota2 = int(input(f"\nIngrese de nuevo la nota N°2 del alumno N°{alumcon}: "))

    nota3 = int(input(f"Ingrese la nota N°3 del alumno N°{alumcon}: "))
    while nota3 < 1 or nota3 > 10 :
        print ("ERROR --> La nota N°3 es menor a 0 o mayor a 10")
        nota3 = int(input(f"\nIngrese de nuevo la nota N°3 del alumno N°{alumcon}: "))
    
    prom = (nota1 + nota2 + nota3) / 3
    resultado = round(prom,2)

    if prom >= 6.50 and prom <= 10:
        print (f"El alumno N°{alumcon} con el promedio {resultado} esta aprobado")
        cant_aprobado += 1
    else: 
        print (f"El alumno N°{alumcon} con el promedio {resultado} esta desaprobado")
        cant_desaprobado += 1

print (f"La cantidad de alumnos aprobados son {cant_aprobado} y la cantidad de alumnos desaprobados son {cant_desaprobado}")

#Proyecto: N37
#Autor: Agustin Turchetti
#Fecha: 23/06/2023
#Mensaje: "Realizar un programa que permita ingresar 3 notas de un 10 alumnos, calcule el promedio y muestre APROBADO o REPROBADO, Al finalizar debe mostrar la cantidad de APROBADOS y DESAPROBADOS"