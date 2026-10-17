#7. En una llantera se ha establecido una promoción de las llantas marca “Todo Terreno”, dicha 
#promoción consiste en lo siguiente: 
#Si se compran menos de cinco llantas el precio es de $300.000 cada una, de $250.000 si se compran 
#de cinco a 10 y de $200.000 si se compran más de 10. 
#Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que 
#compre.

llantas = int(input("INGRESA EL NUMERO DE LLANTAS COMPRADAS: "))

if llantas < 5:
    precio = 300000
elif llantas <= 10:
    precio = 250000
else:
    precio = 200000

total = precio * llantas

print(f"Precio por llanta: ${precio}")
print(f"Total a pagar: ${total}")
