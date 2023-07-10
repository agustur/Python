print ("Calcular descuento en compras mayores a 1000$")

print ("\nSolo descuentos en compras superiores a 1000$")

compra = float(input("\nIngrese el total de su compra: "))

while compra <= 0:
    print ("\nError ==> El valor de total de su compra es menor o igual a 0")
    compra = float(input("\nIngrese el total de su compra: "))

if compra >= 1000:
    descuento = (compra * 10) / 100
    total = compra - descuento
    print ("\nEl valor total de su compra con descuento es de: ", total)
    
else:
    print ("\nNo se aplico descuento porque su valor es menor a 1000$, el total seria: ", compra)

#Proyecto: N24
#Autor: Agustin Turchetti
#Fecha: 19/05/2023
#Mensaje: "Realizar un programa que permita ingresar el total de una venta, si es mayor a 1000 realizar un descuento del 10 %"
