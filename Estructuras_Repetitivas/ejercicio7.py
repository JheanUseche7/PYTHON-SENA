# 7. La oficina de tránsito de Ibagué desea saber, de los n autos
# que entran a la ciudad de Ibagué, cuántos entran con calcomanía
# de cada color.
#
# Conociendo el último dígito de la placa de cada carro,
# se puede determinar el color de la calcomanía utilizando
# la siguiente relación:
#
# Dígito 1 o 2  -> Calcomanía amarilla
# Dígito 3 o 4  -> Calcomanía rosa
# Dígito 5 o 6  -> Calcomanía roja
# Dígito 7 o 8  -> Calcomanía verde
# Dígito 9 o 0  -> Calcomanía azul
#
# Elaborar un programa que permita ingresar los datos de los autos
# y muestre cuántos vehículos corresponden a cada color de calcomanía.


amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0

opcion = 0

while opcion != 3:

    print(" MENU ")
    print("1. Registrar autos")
    print("2. Ver resultados")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        n = int(input("Ingrese la cantidad de autos: "))
        for i in range(n):
            digito = int(input(f"Ingrese el último dígito de la placa del auto {i+1}: "))
            if digito == 1 or digito == 2:
                amarilla += 1
            elif digito == 3 or digito == 4:
                rosa += 1
            elif digito == 5 or digito == 6:
                roja += 1
            elif digito == 7 or digito == 8:
                verde += 1
            elif digito == 9 or digito == 0:
                azul += 1
        print("Datos registrados correctamente")

    elif opcion == 2:
        print(" RESULTADOS ")
        print("Amarilla:", amarilla)
        print("Rosa:", rosa)
        print("Roja:", roja)
        print("Verde:", verde)
        print("Azul:", azul)

    elif opcion == 3:
        print("Gracias por utilizar el sistema")
    else:
        print("Opcion no valida")
