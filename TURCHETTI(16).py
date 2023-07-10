print ("Partido Azul, Partido Unido y Partido Libre")

Pa = int(input("\nIngrese la cantidad de votos del Partido Azul: "))

Pu = int(input("Ingrese la cantidad de votos del Partido Unido: "))

Pl = int(input( "Ingrese la cantidad de votos del Partido Libre: "))

Total = Pa + Pu + Pl
Por1 = Pa / Total * 100
Por2 = Pu / Total * 100
Por3 = Pl / Total * 100

print ("\nCantidad de votos total: ", Total,", Porcentaje del Partido Azul: ", Por1,", Porcentaje del Partido Unido: ", Por2, ", Porcentaje del Partido Libre", Por3)

#Proyecto: N16
#Autor: Agustin Turchetti
#Fecha: 05/05/2023
#Mensaje: "Diseñar un programa que permita ingresar los votos obtenidos en una elección de los partidos Partido azul, Partido unido y Partido libre. Debe calcular y mostrar el total de votos y el porcentaje obtenido por cada partido."