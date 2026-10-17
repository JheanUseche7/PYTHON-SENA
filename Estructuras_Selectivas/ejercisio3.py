#Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de 
#bolsos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para 
#pagar al fabricante: 
# Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad 
#de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al 
#banco un 30% y el resto lo pagará solicitando un crédito al fabricante. 
# Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad 
#de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando 
#crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre 
#la cantidad que se le pague a crédito. 
#Imprimir el valor invertido de su propio dinero, el valor prestado al banco, y el valor del crédito 
#solicitado al fabricante, según sea el caso.

print("Hola, ingresa los siguientes datos")

piezas = int(input("Ingrese el número de piezas compradas: "))
precio = int(input("Ingrese el precio por pieza: "))

monto_total = piezas * precio

if monto_total > 500000:
    print("Dinero invertido propio 55%")
    invertir = monto_total * 0.55
    banco = monto_total * 0.30
    credito_fabricante = monto_total - invertir - banco
else:
    print("Dinero invertido propio %70")
    invertir = monto_total * 0.70
    banco = 0
    credito_fabricante = monto_total * 0.30
intereses = credito_fabricante*0.20
    
print(f"Dinero propio invertido: {invertir}")
print(f"Préstamo del banco: {banco}")
print(f"interes del fabricante: {intereses}")
print(f"Crédito del fabricante: {credito_fabricante}")

   


