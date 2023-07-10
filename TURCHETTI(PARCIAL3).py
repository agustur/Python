print ("Parcial 3")

acumenor = 0
acumayor = 0

for alumno in range (1,11):
    edad = int(input(f"\nIngrese la edad del alumno N°{alumno}: "))
    if edad < 18:
        acumenor = acumenor + 1
    
    else:
        acumayor = acumayor + 1

menorporcen = (acumenor * 100) / alumno
mayorporcen = (acumayor * 100) / alumno
print (f"\nLa cantidad de personas menores son {menorporcen}% ({acumenor} menores) y la cantidad de personas mayores son {mayorporcen}% ({acumayor} mayores)")

#Nombre: Agustin Turchetti
#Trabajo: Parcial 3
