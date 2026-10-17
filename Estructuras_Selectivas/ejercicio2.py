#Calcular el total a pagar por la compra de zapatillas. Si se compran tres  o más zapatillas se 
#aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas un 
#descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y el 
#valor a pagar una vez aplicado el descuento

print ("SISTEMA DE DESCUENTO")
num_zapatillas = int(input("Cantidad de zapatillas compradas: ")) 
valor1= int(input("INGRESE EL PRECIO DE LAS ZAPATILLAS: "))
if num_zapatillas >= 3:
    print("El usuario aplica un descuento del 20%")
    descuento = int(valor1*0.20)
    valor_Desc= valor1 - descuento
    print("El valor a pagar sin descuento: ",valor1)
    print ("El valor con descueto es de: ",valor_Desc)
    print ("El valor del descuento es de: ",descuento)
elif num_zapatillas <= 2:
    print("El usuario aplica un descuento del 10%")
    descuento = int(valor1*0.10)
    valor_Desc = valor1-descuento
    print(" El valor a pagar sin descuento: ",valor1)
    print ("El valor con descueto es de: ",valor_Desc)
    print ("El valor del descuento es de: ",descuento)

print("GRACIAS POR SU COMPRA")
