print ("Menu de opciones")

print ("\n1)Suma de numeros","\n2)Potencia de un numero","\nCalculo de 20% de un numero")

op = int(input("Elija una de las 3 opciones: "))

while op < 1 and op > 3:
    print ("ERROR --> Opcion invalida, Elija una de las opciones entre los valores(1-3)")
    
    print ("\n1)Suma de numeros","\n2)Potencia de un numero","\n3)Calculo de 20% de un numero")
    
    op = int(input("Elija una de las 3 opciones: "))
    
if op == 1:
    print ("Eligío la opcion 1(Suma de numeros)")
    
    num1 = float(input("\nIngrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    
    suma = num1 + num2
    
    print (f"\nEl resultado de la suma es {suma}")
    
elif op == 2:
    print ("Eligío la opcion 2(Potencia 2 de numeros)")
    
    num1 = float(input("\nIngrese el numero: "))
    
    pot = num1 ** 2
    
    print (f"\nEl resultado de la potencia es {pot}")
    
elif op == 3:
    print ("Eligío la opcion 3(Calculo de 20% de un numero)")
    
    num1 = float(input("\nIngrese el numero: "))
    porcen = num1 * 0.20
    
    print (f"\nEl 20% de {num1} es {porcen}")