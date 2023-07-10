#Programa: N°7
#Autor: Agustin Turchetti
#Fecha: 28/04/23
#Mensaje: Ingresar la nota de un alumno y mostrar si es ML, L o P

print ("Nota de alumnos")

N = int(input("Ingrese la nota del alumno: "))

if N >= 9:
    print ("La nota del alumno es un Muy Logrado")
if N >= 7 and N < 9:
    print ("La nota del alumno es un Logrado ")
if N < 7:
    print ("La nota del alumno es un Pendiente")

print ("\nNota de alumnos(como lo haria yo")

N1 = float(input("Ingrese la nota del alumno: "))

if N1 >= 8.51:
    print ("La nota del alumno es un Muy Logrado")
if N1 >= 6.51 and N1 < 8.51:
    print ("La nota del alumno es un Logrado ")
if N1 < 6.51:
    print ("La nota del alumno es un Pendiente")
