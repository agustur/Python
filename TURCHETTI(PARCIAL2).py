print ("Pintureria Color Norte sistema de descuentos")

print ("\nDescuento de 10% en ventas superiores a 5000\nDescuento de 20% en compras superiores a 10000")

nombre = str(input("\nIngrese el nombre del Cliente: "))
apellido = str(input("Ingrese el apellido del Cliente: "))

venta = float(input("Ingrese el total de la venta: "))

while venta <= 0:
    print ("\nERROR --> El total a pagar que ingreso es igual o menor a 0, ingrese un valor permitido(>1)")
    venta = float(input("Ingrese el total de la venta: "))
           
con = nombre + " " + apellido

if venta < 5000:
    des = 0
    totpag = venta - des
    print ("\nVenta del cliente: ",con,"\n","Total de venta: ",venta," Pesos","\n","Descuento: ",des," Pesos","\n","Total a pagar: ",totpag," Pesos")

elif venta >= 5000 and venta < 10000:
    des = (venta * 10) / 100
    totpag = venta - des
    print ("\nVenta del cliente: ",con,"\n","Total de venta: ",venta," Pesos","\n","Descuento: ",des," Pesos","\n","Total a pagar: ",totpag," Pesos")

else:
    des = (venta * 20) / 100
    totpag = venta - des
    print ("\nVenta del cliente: ",con,"\n","Total de venta: ",venta," Pesos","\n","Descuento: ",des," Pesos","\n","Total a pagar: ",totpag," Pesos")


#Programa: Evaluacion Python
#Nombre y Apellido: Agustin Alexander Turchetti Sahajdachy
#Fecha: 02/06/23
#Mensaje: "Diseñar un Programa utilizando el Lenguaje de Programacion Python que permita resolver lo siguiente: Realizar un descuento de 10% en compras superiores a $5000 y Realizar un descuento en compras superiores a 10000"
