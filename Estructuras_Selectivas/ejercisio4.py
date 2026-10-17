# En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento 
#dependiendo de un color  que se escoge al azar. Si el color de la balota es rojo  el descuento es del 
#15% sobre el total de la compra, la balota es verde el descuento es del 20%. Si  el color es diferente 
#a los indicados no obtendrá descuento.  Imprimir el valor de la compra, el color de la balota, el 
#descuento y el valor a pagar. 


valor = float(input("Ingrese el valor de la compra: "))
balota = input("Ingrese el color de la balota: ")

if balota == "rojo":
    descuento = valor * 0.15
elif balota == "verde":
    descuento = valor * 0.20
else:
    descuento = 0

pagar = valor - descuento

print("Valor de la compra:", valor)
print("Color de la balota:", balota)
print("Descuento:", descuento)
print("Valor a pagar:", pagar)