print ("Ejercicio 30")

print ("Cotizacion del dolar = 490 pesos\nCotizacion del euro = 250 pesos")

pesos = int(input("\nIngrese los pesos que tiene: "))

dolarcal = pesos / 490
eurocal = pesos / 250


print ("\nUsted tiene ", pesos, " pesos, el equivalente en dolares seria","{:.2f}".format(dolarcal), " dolares y su equivalente seria de ","{:.2f}".format(eurocal), " euros")

#Proyecto: N30
#Autor: Agustin Turchetti
#Fecha: 09/06/2023
#Mensaje: "Diseñar un programa que permita ingresar un valor en pesos y muestre su equivalente en dólares y euros."