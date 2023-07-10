print ("10 alumnos 10 notas reprobado aprobado")

for i in range (1,11,1):
    nom = str(input("\nIngrese el nombre del alumno: "))
    nota = float(input("Ingrese la nota del alumno: "))
    
    while nota < 1 and nota > 10:
        print ("ERROR --> Solo se pueden poner numeros del 1 al 10")
        nota = float(input("Ingrese la nota del alumno: "))
        
    if nota >= 6.50 and nota <= 10:
        x = "Aprobado"
    elif nota <6.50:
        x = "Desaprobado" 
    print (f"Nombre: {nom} , Nota: {nota}, Situacion: {x}")
        
#Proyecto: N35
#Autor: Agustin Turchetti
#Fecha: 09/06/2023(17/06/23)
#Mensaje: "Realizar un programa que permita ingresar el nombre y la nota final de 10 alumnos y muestre si están APROBADO o DESAPROBADO."