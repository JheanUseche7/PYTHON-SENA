#6.  Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: si 
#el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, se le hará un 
#descuento del 30% sobre la pensión; si el promedio obtenido es menor que 4.0 deberá pagar la 
#pensión completa, la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno.

print("BIENVENIDO")
promedio = float(input("Ingresa el promedio del alumno: "))
valor_pen = float(input("Ingresa el precio de la pension: "))
if promedio >= 4.0:
    print("Reciviras un descuento en la pension del 30%")
    descuento = valor_pen*0.30
    pagar = valor_pen-descuento
    print("valor a pagar es de: ",pagar)
else:
    print("Debes pagar la pension completa que incluye el 10% IVA")
    Valor_iva = valor_pen*0.10
    pagar= valor_pen + Valor_iva

    print(" el valor a pagar es de:", pagar)

