#Programa: N°10
#Autor: Agustin Turchetti
#Fecha: 28/04/23
#Mensaje: Ingresar las notas de 3 un alumno. Calcular y mostrar el promedio del mismo

print ("Notas y Promedio de un alumno")

A = str(input("\nIngrese el nombre del alumno: "))
N1 = float(input("Ingrese la Nota N°1 del alumno: "))
N2 = float(input("Ingrese la Nota N°2 del alumno: "))
N3 = float(input("Ingrese la Nota N°3 del alumno: "))

S = N1 + N2 + N3
P = S / 3

print ("\nEl promedio del Alumno", A, "es: ", P)
