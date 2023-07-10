#Programa: N°11
#Autor: Agustin Turchetti
#Fecha: 28/04/23
#Mensaje: Una estacion meteorologica registra las temperaturas de todos los dias de la semana. Calcula y mostrar el promedio

print ("Promedio de temperaturas")

TD1 = float(input("\nIngrese la temperatura del primer dia en grados centigrados: "))
TD2 = float(input("Ingrese la temperatura del segundo dia en grados centigrados: "))
TD3 = float(input("Ingrese la temperatura del tercero dia en grados centigrados: "))
TD4 = float(input("Ingrese la temperatura del cuarto dia en grados centigrados: "))
TD5 = float(input("Ingrese la temperatura del quinto dia en grados centigrados: "))
TD6 = float(input("Ingrese la temperatura del sexto dia en grados centigrados: "))
TD7 = float(input("Ingrese la temperatura del septimo dia en grados centigrados: "))

S = TD1 + TD2 + TD3 + TD4 + TD5 + TD6 + TD7
P = S / 7

print ("\nEl promedio de la temperatura semanal es: ", P, "°C")
