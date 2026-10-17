# Pedir la cantidad de llantas
llantas = int(input("INGRESA EL NUMERO DE LLANTAS COMPRADAS: "))

# Determinar el precio de cada llanta
if llantas < 5:
    precio = 300000
elif llantas <= 10:
    precio = 250000
else:
    precio = 200000

# Calcular el total a pagar
total = precio * llantas

# Calcular cuánto se ahorró en comparación con el precio más alto
ahorro = (300000 - precio) * llantas

# Mostrar resultados
print(" FACTURA ")
print("Llantas compradas:", llantas)
print("Precio por llanta: $", precio)
print("Total a pagar: $", total)

# Mostrar el ahorro si aplica
if ahorro > 0:
    print("Ahorro obtenido: $", ahorro)

# Mostrar información sobre el descuento
if llantas < 5:
    print("No aplica descuento.")
    print("Si compras 5 llantas, el precio baja a $250000 cada una.")
elif llantas <= 10:
    print("Se aplicó el descuento de compra media.")
    print("Si compras más de 10 llantas, el precio baja a $200000 cada una.")
else:
    print("Se aplicó el descuento máximo.")

